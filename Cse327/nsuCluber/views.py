from django.shortcuts import render

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

def reservation(request):

     #This function is use to display reservation page of our website and retrive some some data from database

    context = {
     # this is for database
    }
    return render(request,'reservation.html',context)

def chatbox(request):
    # This function is use to display chat box page of our website and retrive some some data from database

    context = {
        # this is for database
    }
    return render(request, 'chat-box.html', context)

