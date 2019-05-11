from django.shortcuts import render
from .models import Post



def home(request):
    context = {
        'posts': Post.objects.all()
        #first one key
        #second one value assign to key list of posts dictionaries  created at the top
    }
    return render(request,'blog/home.html',context)
    #in the backend render function will run HttpResponse
def about(request):
    return render(request,'blog/about.html',{'title' : about})