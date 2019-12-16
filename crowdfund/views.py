# coding=utf-8
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Item, User, Investor
from django.http import JsonResponse
from tkinter import Entry

# Create your views here.
from crowdfund import models
from .forms import RegisterForm, LoginForm, AddForm, YdtForm, InvestorForm
import hashlib


def index(request):
    pass
    return render(request, 'index.html')


def thefirst(request):
    pass
    return render(request, 'thefirst/thefirst.html')


def myself(request):
    pass
    return render(request, 'myself/myself.html')


def ydt(request):
    pass
    return render(request, 'ydt/ydt.html')


def touzi(request):
    pass
    return render(request, 'touzi/touzi.html')


def xiangmu(request):
    pass
    return render(request, 'xiangmu/xiangmu.html')


def login(request):
    pass
    return render(request, 'login/login.html')


def guide(request):
    pass
    return render(request, 'guide/guide.html')


def search(request):
    pass
    return render(request, 'search/search.html')


def investor(request):
    pass
    return render(request, 'investor/investor.html')


def choose(request):
    pass
    return render(request, 'search/choose.html')


# 注册函数
def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            userName = register_form.cleaned_data['userName']
            phone = register_form.cleaned_data['phone']
            userPwd = register_form.cleaned_data['userPwd']
            userPwd_new = register_form.cleaned_data['userPwd_new']
            if userPwd != userPwd_new:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'regist/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(userName=userName)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'regist/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.userName = userName
                new_user.userPwd = hash_code(userPwd)
                new_user.phone = phone
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'regist/register.html', locals())


# 数据验证
# 登陆 在数据库中查询用户，然后进行密码比对
def login(request):
    # if request.session.get('is_login', None):  # 避免重复登陆
    # return redirect("/thefirst/")
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            userName = login_form.cleaned_data['userName']
            userPwd = login_form.cleaned_data['userPwd']
            try:
                user = models.User.objects.get(userName=userName)
                if user.userPwd == hash_code(userPwd):  # 哈希值和数据库内的值进行比对
                    # request.session['is_login'] = True  # 向session字典内写入用户状态和数据
                    # request.session['user_id'] = user.id
                    request.session['user_name'] = user.userName
                    return redirect('/thefirst/')
                else:
                    message = "用户名或密码错误！"  # 密码错误
            except:
                message = "用户名或密码错误！"  # 用户名不存在
        return render(request, 'login/login.html', locals())

    login_form = LoginForm()
    return render(request, 'login/login.html', locals())


# 密码加密
def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


# 显示发布项目页面
def add(request):
    pass
    return render(request, 'add/add.html')


# 提交发布项目信息
def add(request):
    if request.method == 'POST':
        add_form = AddForm(request.POST)
        if add_form.is_valid():  # 获取数据
            title = add_form.cleaned_data['title']
            short_title = add_form.cleaned_data['short_title']
            ind_id = add_form.cleaned_data['ind_id']
            country = add_form.cleaned_data['country']
            phase = add_form.cleaned_data['phase']
            amount = add_form.cleaned_data['amount']
            transfer_ratio = add_form.cleaned_data['transfer_ratio']
            phone = add_form.cleaned_data['phone']
            summary = add_form.cleaned_data['summary']
            link_url = add_form.cleaned_data['link_url']
            same_phone_user = models.User.objects.filter(phone=phone)
            if same_phone_user:  # 存在该手机号码
                if title and short_title and ind_id and country:  # 不为空
                    if phase and amount and transfer_ratio and phone and summary:  # 不为空
                        if link_url or link_url[:6] == 'http://':
                            # 满足条件，添加数据
                            new_item = models.Item.objects.create()
                            new_item.title = title
                            new_item.short_title = short_title
                            new_item.ind_id = ind_id
                            new_item.country = country
                            new_item.phase = phase
                            new_item.amount = amount
                            new_item.transfer_ratio = transfer_ratio
                            new_item.summary = summary
                            new_item.link_url = link_url

                            new_item.save()
    add_form = AddForm()
    return render(request, 'add/add.html', locals())


# 用户投资
@csrf_exempt
def ydt(request):
    if request.method == "POST":
        ydt_form = YdtForm(request.POST)
        if ydt_form.is_valid():
            inflow_funds = ydt_form.cleaned_data['inflow_funds']
            # 业务表添加
            new_item = models.Business.objects.create()
            new_item.inflow_funds = inflow_funds
            new_item.save()
            return render(request, 'ydt/ydt.html', locals())
    ydt_form = YdtForm()
    return render(request, 'ydt/ydt.html', locals())


# 项目展示
def xiangmu(request):
    all_item = Item.objects.all()
    return render(request, 'xiangmu/xiangmu.html', {'all_item': all_item})

# 搜索
# def search_top(request):
#    q = request.GET.get('q')
#    error_msg = ''
#    if not q:
#        error_msg = '请输入关键词'
#        return render(request, 'ydt/ydt.html', {'error_msg':error_msg})
#    post_list = User.obj.filter(title_icontains=q)
#    return render(request, 'ydt/ydt.html',{'error_msg':error_msg,''})


# 上传头像
def myself_img(request):
    if request.method == 'POST':
        avatar = request.FILES.get('avatar')

        try:
            models.User.objects.create(avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}

        return JsonResponse(data)

    return render(request, 'myself/myself.html')
def xiangmu_img(request):
    if request.method == 'POST':
        avatar = request.FILES.get('avatar')

        try:
            models.User.objects.create(avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}

        return JsonResponse(data)

    return render(request, 'xiangmu/xiangmu.html')
def touzi_img(request):
    if request.method == 'POST':
        avatar = request.FILES.get('avatar')

        try:
            models.User.objects.create(avatar=avatar)
            data = {'state': 1}
        except:
            data = {'state': 0}

        return JsonResponse(data)

    return render(request, 'touzi/touzi.html')


# 用户投资账户管理
def investor(request):
    if request.method == "POST":
        investor_form = InvestorForm(request.POST)
        if investor_form.is_valid():
            expenditure = investor_form.cleaned_data['expenditure']
            recharge = investor_form.cleaned_data['recharge']
            phone = investor_form.cleaned_data['phone']
            state = investor_form.cleaned_data['state']
            same_phone_user = models.User.objects.filter(phone=phone)
            if same_phone_user:  # 存在该手机号码
                new_investor = models.Investor.objects.create()
                new_investor.disposable_funds = disposable_funds + recharge - expenditure
                new_investor.expenditure = expenditure
                new_investor.recharge = recharge
                new_investor.state = state
                new_investor.save()
                return redirect('/myself/')
    investor_form = InvestorForm()
    return render(request, 'investor/investor.html', locals())


# 用户金额显示
def touzi_show(request):
    all_investor = Investor.objects.all()
    return render(request, 'touzi/touzi.html', {'all_investor': all_investor})


# 项目进展显示
# def ydt_show(request):
