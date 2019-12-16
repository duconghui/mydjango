from django import forms


class RegisterForm(forms.Form):
    userName = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    userPwd = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    userPwd_new = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))


class LoginForm(forms.Form):
    userName = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    userPwd = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class AddForm(forms.Form):
    SELVALUE_ind_id = (
        ('移动互联', 'one'),  # 前面是展示在前端界面的内容,后面的'first'是真正存在数据库中的
        ('节能环保', 'two'),
        ('文化传媒', 'three'),
        ('新能源', 'four'),
        ('消费服务', 'five'),
        ('其他', 'six'),
    )
    ind_id = forms.CharField(max_length=10, widget=forms.widgets.Select(choices=SELVALUE_ind_id))
    SELVALUE_country = (
        ('北京', 'one'),  # 前面是展示在前端界面的内容,后面的'first'是真正存在数据库中的
        ('天津', 'two'),
        ('浙江', 'three'),
        ('上海', 'four'),
        ('福建', 'five'),
        ('湖北', 'six'),
        ('其他', 'seven'),
    )
    country = forms.CharField(max_length=10, widget=forms.widgets.Select(choices=SELVALUE_country))  # 项目地区
    SELVALUE_phase = (
        ('种子期', 'one'),  # 前面是展示在前端界面的内容,后面的'first'是真正存在数据库中的
        ('成长期', 'two'),
        ('扩张期', 'three'),
        ('成熟期', 'four'),
    )
    phase = forms.CharField(max_length=10, widget=forms.widgets.Select(choices=SELVALUE_phase))  # 项目阶段
    title = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    short_title = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    amount = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    transfer_ratio = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    link_url = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    summary = forms.CharField(max_length=40, widget=forms.Textarea(attrs={'class': 'form-control'}))


class YdtForm(forms.Form):
    inflow_funds = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))


class InvestorForm(forms.Form):
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    recharge = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    expenditure = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    SELVALUE_state = (
        ('认证成功', 'one'),  # 前面是展示在前端界面的内容,后面的'one'是真正存在数据库中的
        ('未认证', 'two'),
    )
    state = forms.CharField(max_length=10, widget=forms.widgets.Select(choices=SELVALUE_state))
