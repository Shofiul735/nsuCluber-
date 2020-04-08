ffrom django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('admin-dash',views.adminDash,name='admin'),
    path('reservation',views.reservation,name='reservation')
]
