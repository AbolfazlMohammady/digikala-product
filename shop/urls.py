from django.urls import path

from .views import *

urlpatterns = [
    path('',homeview , name = 'home'),
    path('about/',aboutview , name= 'about'),
    path('login/',login_user , name = 'login'),
    path('logout/',logout_user , name = 'logout'),
    path('singup/',singup_user , name = 'singup'),
    path('product/<int:pk>',product , name = 'product'),
    path('category/<str:cat>',category , name = 'category'),

]
