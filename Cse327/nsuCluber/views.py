from django.shortcuts import render

# Create your views here.

def reservation(request):
    '''
      This function is use to display reservation page of our website and retrive some some data from database
    '''
    context = {
    
    }
    return render(request,'reservation.html',context)
