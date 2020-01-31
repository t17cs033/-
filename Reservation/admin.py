from django.contrib import admin
from .models import Member,Reserve,MeetingRoom,Facility,Billing

def has_delete_permission(self,request,obj=None):
    return False
admin.ModelAdmin.has_delete_permission = has_delete_permission

# Register your models here.
admin.site.register(Member)
admin.site.register(Reserve)
admin.site.register(MeetingRoom)
admin.site.register(Facility)
admin.site.register(Billing)