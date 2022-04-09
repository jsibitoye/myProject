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
   path('logouts', views.logouts, name='logouts'),
   #path('userpost/<str:pk>', views.userpost, 'userpost') # note the /str: pk, it means we want this line to call userpost in view but send in a parameter named pk.
   path('post/<str:pk>', views.post,name='post'),
   path('userpost',views.userpost, name='userpost')
]