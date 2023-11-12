from django.shortcuts import render
from . models import place, vlog
# Create your views here.
def fun(request):
    places = place.objects.all()
    vlogs = vlog.objects.all()
    return render(request, 'index.html', {'places': places, 'vlogs': vlogs})

def addition(request):
    num1=int(request.POST["num1"])
    num2=int(request.POST["num2"])
    num3=num1+num2
    return render(request,"result.html", {"add": num3})
