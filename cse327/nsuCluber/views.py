from django.shortcuts import render

# Create your views here.

def index(request):
    '''
      This function is use to display home page of our website and retrive some some data from database
    '''
    context = {
     '''
      for retriving database data
     '''
    }
    return render(request,'index.html',context)

def adminDash(request):
    '''
     This function is for admin Dashboard
    '''
    context = {
     '''
      for retriving database data
     '''
    }
    return render(request,'includes/admin-dash.html',context)
