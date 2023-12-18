from django.shortcuts import render,redirect
from django.http import HttpResponse
from pathlib import Path
import os
from app.models import prebooking

# Create your views here.

def Homeview(request):
    return render(request,"Home.html")

def registers(request):
    return render(request,"register.html",{})

def Thanks(request):
    if request.method == 'POST':
        uname = request.POST['name']
        uage = request.POST['age']
        ugender = request.POST['gender']
        umobile= request.POST['mobile']
        uemail = request.POST['email']
        ustarts = request.POST['starts']
        uends = request.POST['ends']
        ustate = request.POST['state']
        udistrict = request.POST['district']
        udistination  = request.POST['distination']
        umem = request.POST['mem']
        uadult = request.POST['adult']
        uchildern = request.POST['children']
        abc=prebooking(Name=uname,Age=uage,Gender=ugender,Mobile_no=umobile,Email_id=uemail,Trip_start_date =ustarts,Trip_end_date=uends, Your_State=ustate,Your_District=udistrict,Distination=udistination,Members_in_Trip=umem,Adults_in_Trip =uadult,Childerns_in_Trip=uchildern)
        abc.save();
    return render(request,"Thank.html")
