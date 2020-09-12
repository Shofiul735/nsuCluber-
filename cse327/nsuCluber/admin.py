from django.contrib import admin
from .models import AllAdmins,ExistingMember,EventPost
# Register your models here.

admin.site.register(AllAdmins)
admin.site.register(ExistingMember)
admin.site.register(EventPost)