from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_Topic(request):
    tn=input('Enter Topic_name')
    To=Topic.objects.get_or_create(Topic_name=tn)[0]
    To.save()
    return HttpResponse('Topic is inserted')

def insert_Webpage(request):
    tn=input('Enter Topic_name')
    To=Topic.objects.get_or_create(Topic_name=tn)[0]
    To.save()
    n=input('Enter name')
    u=input('Enter url')
    Wo=Webpage.objects.get_or_create(Topic_name=To,name=n,url=u)[0]
    Wo.save()
    return HttpResponse('Topic is Webpage')

def insert_AccessRecords(self):
    tn=input('Enter Topic_name')
    To=Topic.objects.get_or_create(Topic_name=tn)[0]
    To.save()
    n=input('Enter name')
    u=input('Enter url')
    Wo=Webpage.objects.get_or_create(Topic_name=To,name=n,url=u)[0]
    Wo.save()
    p=input('Enter date')
    q=input('Enter name')
    AR=AccessRecords.objects.get_or_create(name=Wo,date=p,author=q)[0]
    AR.save()
    return HttpResponse('Topic is AccessRecords page')