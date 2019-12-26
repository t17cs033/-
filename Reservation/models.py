from django.db import models

# Create your models here.

class Member(models.Model):
    cmpId = models.IntegerField()               #ID
    cmpName = models.CharField(max_length = 50) #企業名
    address = models.CharField(max_length = 50) #住所
    tel = models.CharField(max_length = 50)     #電話番号
    section = models.CharField(max_length = 50) #担当部署
    name = models.CharField(max_length = 50)    #担当者名
    mail = models.CharField(max_length = 50)    #メールアドレス
    pay = models.CharField(max_length = 50)     #支払金額
    def __str__(self):
        return self.cmpName
    
class Reserve(models.Model):
    number = models.IntegerField()                  #予約番号
    cmpId = models.IntegerField()                   #ID
    date = models.DateField(blank=False,null=False) #日付
    start_time = models.CharField(max_length = 50)  #利用開始時間
    end_time = models.CharField(max_length = 50)    #利用終了時間
    mrName = models.CharField(max_length = 50)      #会議室名
    fclName = models.CharField(max_length = 50)     #付属設備名
    charge = models.CharField(max_length = 50)      #料金
    def __str__(self):
        return self.number
    
class MeetingRoom(models.Model):
    mrName= models.CharField(max_length = 50)   #会議室名
    avail = models.IntegerField()               #空き数
    charge = models.CharField(max_length = 50)  #料金
    def __str__(self):
        return self.mrName
    
class Facility(models.Model):
    fclName = models.CharField(max_length = 50) #付属設備名
    stock = models.CharField(max_length = 50)   #在庫数
    charge = models.CharField(max_length = 50)  #料金
    
    def __str__(self):
        return self.fclName
    
class Billing(models.Model):
    cmpId = models.IntegerField()               #ID
    amount = models.CharField(max_length = 50)  #請求額
    remain = models.CharField(max_length = 50)  #残高
    def __str__(self):
        return self.cmpId
    