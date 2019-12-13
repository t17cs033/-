from django.db import models

# Create your models here.

class Member(models.Model):
    member_id = models.IntegerField()
    company_name = models.CharField()
    company_address = models.CharField()
    company_tel = models.IntegerField(max_length = 11)
    menber_org = models.CharField()
    menber_name = models.CharField()
    mail = models.CharField()
    payment = models.IntegerField()
    
class Reserve(models.Model):
    rsv_number = models.IntegerField()
    date = models.DateField(blank=False,null=False)
    start_time = models.IntegerField(max_length = 4)
    end_time = models.IntegerField(max_length = 4)
    name_rsvMR = models.CharField()
    name_rsvFcl = models.CharField()
    charge_rsv = models.IntegerField()
    
class MeetingRoom(models.Model):
    name_MR = models.CharField()
    availability = models.IntegerField()
    charge_MR = models.IntegerField()
    
class Facility(models.Model):
    name_facility = models.CharField()
    stock = models.CharField()
    charge_fcl = models.IntegerField()
    
class Billing(models.Model):
    bill_id = models.ImageField()
    amount = models.IntegerField()
    remain = models.IntegerField()
    