
from django.urls import path
from .import views

urlpatterns = [

    path('',views.print,name="index"),
    path('convert/',views.convert,name='convert'),
]