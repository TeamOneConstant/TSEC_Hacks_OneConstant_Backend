from django.urls import path
from integrations.views import *

urlpatterns = [

    path('facebook/post', FacebookIntegrationAPI.as_view(), name="facebook-post"),

]

