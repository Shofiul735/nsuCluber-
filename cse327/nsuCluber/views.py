from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):

     # This function is use to display home page of our website and retrive some some data from database

    context = {
      #this is for database
    }
    return render(request,'index.html',context)

def adminDash(request):

     #This function is for admin Dashboard

    context = {
     # this is for database
    }
    return render(request,'includes/admin-dash.html',context)

def existingMember(request):
     #This function is for existing member views
    if request.POST:
      memType = request.POST['select_mem']
    context = {
     # this is for database and other data
    }
    return render(request,'includes/existingMember.html',context)

def eventPost(request):
  #This function is for event-post.html
  context = {
    #This dictionary for database and others data
    'form':forms.EventPostModelForm
  }
  return render(request,'includes/event-post.html',context)