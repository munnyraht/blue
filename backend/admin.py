from django.contrib import admin
from home.models import HomeData
# Register your models here.
from .models import personalinfo,bvn_details
#admin.site.register(user)
admin.site.register(bvn_details)
admin.site.register(personalinfo)
admin.site.register(HomeData)




