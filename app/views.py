from django.shortcuts import render

# Create your views here.
def fun1(request):
    return render(request,'1.html')

def fun2(request):
    return render(request,'2.html')

def fun3(request):
    return render(request,'3.html')

def fun4(request):
    return render(request,'4.html')
