###################################################
##  DRAFT ## DRAFT ## DRAFT
##
##  Sorting and aglamating json records for easier DTL operaion
##

from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
from proj import settings
import json

# Create your views here.

def test(request):
    path = str(settings.BASE_DIR) + "<br>" + str(settings.NEWS_JSON_PATH)
    with open(settings.NEWS_JSON_PATH) as jf:
        jstring = json.load(jf)
    jdict = {}
    for i in jstring:
        print(i["created"][:10])
        if i["created"][:10] not in jdict:
            jdict[i["created"][:10]] = []
        jdict[i["created"][:10]].append(i)
    #return HttpResponse(jstring)
    return render(request, 'photos/json.html', context = {"a":jdict})

def main(request):
    return render(request, 'photos/main.html')

def base(request):
    return render(request, 'photos/base.html')



