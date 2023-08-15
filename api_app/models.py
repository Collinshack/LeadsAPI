from django.db import models
import uuid
# Create your models here.


class RealEstateLead(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    business_name = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    website = models.URLField(max_length=50)
    address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True, null=True)
    
    


class YoutubeLead(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    email = models.EmailField(max_length=50, unique=True)
    niche = models.CharField(max_length=50)
    subscriber_range = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True, null=True)
    