from django.urls import URLPattern, path
from . import views

urlpatterns  = [
   path('', views.index, name='index'),
   path('josh', views.josh, name='josh'),
#  path('url id according to action, which view, the name you want to give it - may be empty') 
#  so you can have the end result of view.counter pointing back at index.html
   path('counter', views.counter, name='thisCouldBeAnyrthing'),
   path('register', views.register, name='register'),
   path('login', views.login, name='login'),
   path('logout', views.logout, name='logout')
]