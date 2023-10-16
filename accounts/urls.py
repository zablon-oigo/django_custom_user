from django.urls import path
from .views import (sign_in,sign_out,sign_up, update_profile)

urlpatterns=[
    path('login/', sign_in, name='login'),
    path('logout/', sign_out, name='logout'),
    path('register/', sign_up, name='register'),
    path('profile/', update_profile, name='profile')
]