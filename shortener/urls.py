from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('create/', create_short_url, name='create'),
    path('edit/<int:pk>/', edit_short_url, name='edit'),
    path('delete/<int:pk>/', delete_short_url, name='delete'),
    
    # new path added
    path('public-qr/<str:code>/', public_qr_code_png, name='public-qr'),
    path('auth-qr/<str:code>/', auth_qr_code_png, name='auth-qr'),
]
