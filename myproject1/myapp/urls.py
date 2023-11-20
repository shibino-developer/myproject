from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('nine/',views.nine,name='index'),
    path('eight/',views.eight,name='eight'),
    # path('ten/',views.ten,name='ten'),
    path('formview/',views.formview,name='formview'),
    path('viewdata/',views.viewdata,name='viewdata'),
    path('',views.index,name='index'),
    path('twelve/',views.twelve,name='twelve'),
    path('index/',views.index,name='index'),
    path('usercreate/',views.usercreate,name='usercreate')
]