from django.contrib import admin
from .models import Member,Reserve,MeetingRoom,Facility,Billing

# Register your models here.
admin.site.register(Member)
admin.site.register(Reserve)
admin.site.register(MeetingRoom)
admin.site.register(Facility)
admin.site.register(Billing)