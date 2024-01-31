from django.db import models
from accounts.models import CustomUser
from django.db.models.fields.related import ForeignKey

# Create your models here.



class PostHistory(models.Model):

    user = ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    photo = models.CharField(max_length=300, blank=True, null=True)
    text = models.CharField(max_length=2048, blank=True, null=True)

    response = models.JSONField(max_length=100, blank=True, null=True)

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



