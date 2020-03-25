from django.shortcuts import render

# Create your views here.

def index(request):
    '''
      This function is use to display home page of our website and retrive some some data from database
    '''
    context = {
    
    }
    return render(request,'index.html',context)
