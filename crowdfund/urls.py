"""crowdfunding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from crowdfund import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^myself/', views.myself, name='myself'),
    url(r'^thefirst/', views.thefirst, name='thefirst'),
    url(r'^add/', views.add, name='add'),
    url(r'^touzi/', views.touzi, name='touzi'),
    url(r'^investor/', views.investor, name='investor'),
    url(r'^choose', views.choose, name='choose'),
    url(r'^xiangmu', views.xiangmu, name='xiangmu'),
    url(r'^ydt', views.ydt, name='ydt'),
    url(r'^guide', views.guide, name='guide'),
    url(r'^search', views.search, name='search'),
    url(r'^xiaoxi', views.thefirst, name='xiaoxi'),
    url(r'^help', views.guide, name='help'),
]

app_name = 'crowdfund'
