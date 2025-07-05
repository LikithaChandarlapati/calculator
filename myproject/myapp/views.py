from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        a=int(request.POST.get('num1'))
        b=int(request.POST.get('num2'))
        o=request.POST.get('op')
        if o == 'add':
            result=a+b
           
        return render(request,'home.html',{'result':10})
     return render(request,'home.html')
def hello(request):
    return Httpresponse('nirula')
