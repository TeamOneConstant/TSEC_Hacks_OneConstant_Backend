from django.urls import path
from integrations.views import *

urlpatterns = [

    path('post', FacebookIntegrationAPI.as_view(), name="facebook-post"),

]

