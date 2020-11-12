from django.shortcuts import render
from .models import Category, Services, Users, Packages, Reports, Comments
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .modules.api import API
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def index(request):
    context={
        "categories":Category.objects.values("id","name")
    }
    return render(request,"index.html", context=context)

def services(request):
    services=Services.objects.filter(visibility=1).values('id', 'name','thumbnail','url','normal_rate', 'has_packages', 'category','user')
    for service in services:
        userInstance=Users.objects.get(id=service['user'])
        categoryInstance=Category.objects.get(id=service['category'])
        service['user']=userInstance.full_names
        service['category']=categoryInstance.name
    context={
        'title':'All services',
        'services': services
    }
    return render(request, 'services.html', context=context)

def specificService(request, url):
    service=Services.objects.get(url=url)
    context={
        'service':service
    }
    if service.has_packages:
        context['packages']=Packages.objects.filter(service=service.id)
    
    # get other service
    otherServices=Services.objects.filter(user=service.user)[:5]
    context['otherServices']=otherServices


    return render(request, 'specific-service.html', context)

def report(request):
    try:
        serviceInstance=Services.objects.get(url=request.POST['url'])
        reportInstance=Reports(service=serviceInstance, email=request.POST['email'], details=request.POST['details'])
        reportInstance.save()

        messages.success(request, "Report received successfully. We shall act accordingly")
    except Exception as e:
        messages.error(request, "Error receiving report. Please contact customer care for assistance")

    return HttpResponseRedirect(reverse("specificService", args=[request.POST['url']]))

def comment(request):
    try:
        serviceInstance=Services.objects.get(url=request.POST['url'])
        commentInstance=Comments(service=serviceInstance, email=request.POST['email'], comment=request.POST['comment'])
        commentInstance.save()

        messages.success(request, "Comment received successfully.")
    except Exception as e:
        messages.error(request, "Error receiving comment. Please contact customer care for assistance")

    return HttpResponseRedirect(reverse("specificService", args=[request.POST['url']]))

def filterByCategory(request, id):
    context={}
    try:
        services=Services.objects.filter(category=id).values('id', 'name','thumbnail','url','normal_rate', 'has_packages', 'category','user')
        for service in services:
            userInstance=Users.objects.get(id=service['user'])
            categoryInstance=Category.objects.get(id=service['category'])
            service['user']=userInstance.full_names
            service['category']=categoryInstance.name

        context['title']="{} services".format(categoryInstance.name)
        context['services']=services

    except:
        context['error']="Error retrieving services. Please try again later"

    return render(request, 'services.html', context=context)

def searchForServices(request):
    context={}
    if request.POST:
        services=Services.objects.filter(name__icontains=request.POST['service']).values('id', 'name','thumbnail','url','normal_rate', 'has_packages', 'category','user')
        for service in services:
            userInstance=Users.objects.get(id=service['user'])
            categoryInstance=Category.objects.get(id=service['category'])
            service['user']=userInstance.full_names
            service['category']=categoryInstance.name

        context['title']="Search results for {}".format(request.POST['service'])
        context['services']=services

        return render(request, 'services.html', context=context)


@api_view(['POST'])
def api(request):
    responseData=API(request.data).api()
    response=Response(responseData)

    return response