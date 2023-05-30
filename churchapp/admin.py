# type:ignore
from django.contrib import admin
from .models import Profile,Admin,Client


admin.site.register(Profile)
admin.site.register(Client)
admin.site.register(Admin)