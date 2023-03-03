from django.urls import path
from . import views
app_name='app1'
urlpatterns=[
    path('hello/',views.hello,name='hello'),
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
]