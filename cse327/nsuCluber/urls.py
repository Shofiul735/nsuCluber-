from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('admin-dash/',views.adminDash,name='admin'),
    path('admin-dash/existing-member/',views.existingMember,name = "existingMember"),
    path('admin-dash/event-post',views.eventPost,name = "eventPost")
]
