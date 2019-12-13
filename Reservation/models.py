from django.db import models

# Create your models here.

class Member(models.Model):
    member_id = models.IntegerField()
    company_name = models.CharField(max_length = 50)
    company_address = models.CharField(max_length = 50)
    company_tel = models.IntegerField()
    menber_org = models.CharField(max_length = 50)
    menber_name = models.CharField(max_length = 50)
    mail = models.CharField(max_length = 50)
    payment = models.IntegerField()
    
class Reserve(models.Model):
    rsv_number = models.IntegerField()
    date = models.DateField(blank=False,null=False)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    name_rsvMR = models.CharField(max_length = 50)
    name_rsvFcl = models.CharField(max_length = 50)
    charge_rsv = models.IntegerField()
    
class MeetingRoom(models.Model):
    name_MR = models.CharField(max_length = 50)
    availability = models.IntegerField()
    charge_MR = models.IntegerField()
    
class Facility(models.Model):
    name_facility = models.CharField(max_length = 50)
    stock = models.CharField(max_length = 50)
    charge_fcl = models.IntegerField()
    
class Billing(models.Model):
    bill_id = models.ImageField()
    amount = models.IntegerField()
    remain = models.IntegerField()
    