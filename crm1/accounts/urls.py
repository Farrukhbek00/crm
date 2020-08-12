from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('user/', views.user, name='user'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<int:pk>/', views.customer, name='customer'),
    path('update_order/<int:pk>/', views.update_order, name='update-order'),
    path('delete_order/<int:pk>/', views.delete_order, name='delete-order'),
    path('create_order/<int:pk>/', views.create_order, name='create-order'),
]
