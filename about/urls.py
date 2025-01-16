from . import views
from django.urls import path

urlpatterns = [
    path('', views.AdminList.as_view(), name='home'),
    path('<str:title>/', views.post_detail, name='about_title'),
]