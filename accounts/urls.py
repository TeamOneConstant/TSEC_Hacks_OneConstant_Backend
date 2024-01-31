from django.urls import path
from accounts.views import *

urlpatterns = [

    path('login', UserLogin.as_view(), name="login")

]

