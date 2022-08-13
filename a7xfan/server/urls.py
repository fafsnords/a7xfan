from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('forum/', views.forum, name='forum'),
    path('log_out/', views.log_out, name='log_out')
]