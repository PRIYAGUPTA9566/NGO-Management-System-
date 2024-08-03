from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from datetime import datetime

from django.http import HttpResponse

# Create your views here.
def index(request):
    sdata=slider.objects.all().order_by('-id')[0:3]
    udata=upcommingevent.objects.all().order_by('-id')[0:6]
    vdata=volunteer.objects.all().order_by('email')[0:6]
    ddata=donate.objects.all().order_by('-id')[0:6]
    mydict={"sd":sdata,"udata":udata,"vdata":vdata,"ddata":ddata}
    return render(request,'user/index.html',mydict)

def vision(request):
    return render(request,'user/OurVision.html')

def stories(request):
    scdata=schange.objects.all().order_by('-id')
    md={"scdata":scdata}
    return render(request,'user/storiesofchange.html',md)

def ourvolunteers(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        cposition=request.POST.get('cposition')
        picture=request.FILES['fu']
        x=volunteer.objects.filter(email=email).count()
        if x==0:
            volunteer(name=name,email=email,mobile=mobile,city=address,current_position=cposition,picture=picture).save()
            return HttpResponse("<script>alert('You are registered Successfully..');location.href='/user/volunteers/'</script>")
        else:
            return HttpResponse("<script>alert('You are already registered..');location.href='/user/volunteers/'</script>")
    return render(request,'user/volunteers.html')

def upcomingevent(request):
    data=upcommingevent.objects.all().order_by('-id')
    md={"eventdata":data}
    return render(request,'user/upcommingevent.html',md)

def need(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        picture=request.POST.get('picture')
        htype=request.POST.get('helptype')
        message=request.POST.get('message')
        addess=request.POST.get('address')
        nhelp(name=name,mobile=mobile,helptype=htype,message=message,addess=addess,picture=picture,request_date=datetime.now().date()).save()
        return HttpResponse("<script>alert('Your request added successfully...');location.href='/user/need/'</script>")
    return render(request,'user/needhelp.html')

def donateus(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        picture=request.POST.get('fu')
        city=request.POST.get('city')
        pincode=request.POST.get('pincode')
        amount=request.POST.get('amount')
        address=request.POST.get('address')
        donate(name=name,picture=picture,mobile=mobile,email=email,city=city,address=address,pincode=pincode,rupees=amount,ddate=datetime.now().date()).save()
        return HttpResponse("<script>alert('Thanks for donating us...');location.href='/user/donateus/'</script>")

    return render(request,'user/donate.html')

def login(request):
    return render(request,'user/login.html')


def contact(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('mobile')
        d=request.POST.get('msg')
        #print(a,b,c,d)
        contactus(name=a, email=b, mobile=c, message=d).save()
        return HttpResponse( "<script>alert('Thanks for contacting with us ...');location.href='/user/contact/'</script>")

    return render(request,'user/contact.html')


def viewevent(request):
    eid=request.GET.get('msg')
    data=upcommingevent.objects.filter(id=eid)
    md={"data":data}
    return render(request,'user/viewevent.html',md)


def volunteerlist(request):

    vid=request.GET.get('vid')
    did=request.GET.get('did')
    ddata="";
    vdata="";
    if vid is not None:
        vdata=volunteer.objects.filter(email=vid)
    elif did is not None:
        ddata=donate.objects.filter(id=did)
    else:
        vdata=volunteer.objects.all()
        ddata=donate.objects.all().order_by('-id')
    md = {
          "vdata":vdata,
          "ddata":ddata
    }
    return render(request,'user/volunteerlist.html',md)