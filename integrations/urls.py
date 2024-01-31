from django.urls import path
from integrations.views import *

urlpatterns = [

    path('post', IntegrationPostAPI.as_view(), name="post"),
    path('add', IntegrationAddPlatformAPI.as_view(), name="add"),


]

