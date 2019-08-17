
from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'credential'

urlpatterns = [
    path('register',register,name='register'),
    path('user_login',user_login,name='user_login'),
    path('logout',user_logout,name="user_logout")
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
