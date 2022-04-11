from ast import Or
from msilib.schema import Class
import re
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Origin
from .models import Champion
import json
# Create your views here.
from getchamp.serializers import *
from rest_framework import viewsets
def TestView(request):
    return HttpResponse("Hello world")


def ImageTest(request):
    q = Champion.objects.all()
    if 'a' in request.GET:
        a = request.GET['a']
        post = Champion.objects.filter(Name__icontains = a)
    else:
        post = Champion.objects.all()
    return render(request, 'getchamp/index.html', {'q':q})

def SearchBar(request):
    #Search by name
    if 'a' in request.GET:
        a = request.GET['a']
        post = Champion.objects.filter(Name__icontains = a)
    else:
        post = Champion.objects.all()
    
    #Origin Filter
    tmp =  str(list(request.GET.keys()))
    tmp = tmp[3:-2]
    tmp = "b"+tmp
    if tmp in request.GET:
        b =  str(list(request.GET.keys()))
        b = b[3:-2]
        post  = Champion.objects.filter(Origin = b)

    
    #Class filter
    cl = str(list(request.GET.keys()))
    cl = cl[3:-2]
    cl = "c" + cl
    if cl in request.GET:
        c = str(list(request.GET.keys()))
        c = c[3:-2]
        post = Champion.objects.filter(Class = c)

    return render(request, 'getchamp/index.html',{'post': post})



def TeamBuilding(request):
    #Search by name
    if 'a' in request.GET:
        a = request.GET['a']
        post = Champion.objects.filter(Name__icontains = a)
    else:
        post = Champion.objects.all()
    
    #Origin Filter
    tmp =  str(list(request.GET.keys()))
    tmp = tmp[3:-2]
    tmp = "b"+tmp
    if tmp in request.GET:
        b =  str(list(request.GET.keys()))
        b = b[3:-2]
        post  = Champion.objects.filter(Origin = b)

    
    #Class filter
    cl = str(list(request.GET.keys()))
    cl = cl[3:-2]
    cl = "c" + cl
    if cl in request.GET:
        c = str(list(request.GET.keys()))
        c = c[3:-2]
        post = Champion.objects.filter(Class = c)
    return render(request, 'getchamp/teambuilder.html',{'post': post})


class APIChampion(viewsets.ModelViewSet):
    queryset = Champion.objects.filter()
    serializer_class = ChampionSerializer


def ChampionInfo(request):
    info = request.GET['xname']
    post = Champion.objects.filter(Name = info)
    return render(request, 'getchamp/champion_info.html', {'post':post})



def TeamName(request):
    if 'text' in request.GET:
        team = request.GET['text']
        team.replace('+',' ')
    else:
        return render(request, 'getchamp/create_team_name.html')
    
    user = User.objects.get(pk = 1)
    b = TeamBuilder(TeamName = team, Player = user)
    b.save()
    return render(request, 'getchamp/create_team_name.html')

def Save(request):
    
    if 'build' in request.GET:
        build = request.GET['build']
    else:
        return render(request, 'getchamp/teambuilder.html')
    
    champ = Champion.objects.get(Name = build)
    champ.team.add()


    return render(request, 'getchamp/teambuilder.html')