from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.
class Member（models.Model):
    member_id = models.IntegerField()
    company_name = models.CharField(max_length = 100)
    company_address = models.CharField(max_length = 200)
    

class Reserve(models.Model):
    temp_text = models.CharField(max_length=200)
    
    