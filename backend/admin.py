from django.contrib import admin

# Register your models here.
from .models import user, personalinfo,bvn_details
admin.site.register(user)
admin.site.register(bvn_details)
admin.site.register(personalinfo)
