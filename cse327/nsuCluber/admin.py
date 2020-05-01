from django.contrib import admin
from .models import AllAdmins,ExistingMember
# Register your models here.

admin.site.register(AllAdmins,ExistingMember)