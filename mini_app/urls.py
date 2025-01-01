
from django.urls import path
from .import views

urlpatterns = [

    path('index/',views.print,name="index"),
    path('convert/',views.convert,name='convert'),
    path('',views.login,name='login'),
    path('reg/',views.register,name="reg"),
    path('regist/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
