from django.contrib import admin
from .models import *

# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','message')
admin.site.register(contactus,contactusAdmin)


class sliderAdmin(admin.ModelAdmin):
    list_display = ('id','headlines','slider_dec','slider_picture')
admin.site.register(slider,sliderAdmin)


class upcommingeventAdmin(admin.ModelAdmin):
    list_display = ('id','event_picture','event_title','event_details','event_date','event_place','event_purpose')
admin.site.register(upcommingevent,upcommingeventAdmin)

class volunteerAdmin(admin.ModelAdmin):
    list_displiay = ('name','email','city','current_position','picture')
admin.site.register(volunteer,volunteerAdmin)


class donateAdmin(admin.ModelAdmin):
    list_display = ('id','name','picture','mobile','email','city','address','pincode','rupees','ddate')
admin.site.register(donate,donateAdmin)


class nhelpAdmin(admin.ModelAdmin):
    list_display = ('id','name','mobile','helptype','message','address','picture','request_date')
admin.site.register(nhelp,nhelpAdmin)


class schangeAdmin(admin.ModelAdmin):
    list_display = ('id','title','picture','description')
admin.site.register(schange,schangeAdmin)



