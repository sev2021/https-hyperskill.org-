from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from pathlib import Path
import json


# Create your views here.
def news(request, news_id):
  jpath = Path(__file__).resolve().parent.parent
  with open(settings.NEWS_JSON_PATH) as jf:
    jstring = json.load(jf)
  for i in jstring:
    if i["link"] == news_id:
      jhttp = f'<h2>{i["title"]}</h2><p>{i["created"]}</p><p>{i["text"]}</p><a target="_blank" target="_blank" href="/news/">A</a>'
      return HttpResponse(jhttp)

  return HttpResponse("NO SUCH WEBISTE")


def news_index(request):
  jpath = Path(__file__).resolve().parent.parent
  with open(settings.NEWS_JSON_PATH) as jf:
    jstring = json.load(jf)
    jstring.sort(key=lambda i:i['created'], reverse=True) # sorting for list of dict
    jcontext = {"jtemplate": {}}
    for i in jstring:
      created_index = i['created'][:10]

      if not created_index in jcontext['jtemplate']:
        jcontext['jtemplate'][created_index] = []
      jcontext['jtemplate'][created_index].append(i)
      print(jcontext)

  return render(request, 'news/news.html', context=jcontext)
