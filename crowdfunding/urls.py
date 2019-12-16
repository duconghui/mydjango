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
    # url(r'^admin/', admin.site.urls),
    url(r'^crowdfund/', include('crowdfund.urls', namespace='crowdfund')),
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^myself/', views.myself),
    url(r'^thefirst/', views.thefirst),
    url(r'^add/', views.add),
    url(r'^touzi/', views.touzi),
    url(r'^investor/', views.investor),
    url(r'^choose', views.choose),
    url(r'^xiangmu', views.xiangmu),
    url(r'^ydt', views.ydt),
    url(r'^guide', views.guide),
    url(r'^search', views.search),
    url(r'^xiaoxi', views.search),
    url(r'^help', views.search),
]
