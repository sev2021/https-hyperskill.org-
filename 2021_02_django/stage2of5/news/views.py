from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from pathlib import Path
import json

# Create your views here.
def news(request, news_id):
    jpath  = Path(__file__).resolve().parent.parent
    with open(settings.NEWS_JSON_PATH) as jf:
        jstring = json.load(jf)
    for i in jstring:
        if i["link"] == news_id:
            jhttp = f'<h2>{i["title"]}</h2><p>{i["created"]}</p><p>{i["text"]}</p><a target="_blank" target="_blank" href="/news/">A</a>'
            return HttpResponse(jhttp)

    return HttpResponse("NO SUCH WEBISTE")