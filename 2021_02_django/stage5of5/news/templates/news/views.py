from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from pathlib import Path
from django.views import View
import json, datetime


# Create your views here.
def news(request, news_id):
  with open(settings.NEWS_JSON_PATH) as jf:
    jstring = json.load(jf)
  for i in jstring:
    if i["link"] == news_id:
      jhttp = f'<h2>{i["title"]}</h2><p>{i["created"]}</p><p>{i["text"]}</p><a target="_blank" target="_blank" href="/news/">A</a>'
      return HttpResponse(jhttp)

  return HttpResponse("NO SUCH WEBISTE")


def news_index(request):
  nsearch = request.GET.get('q')
  with open(settings.NEWS_JSON_PATH) as jf:
    jstring = json.load(jf)
    jstring.sort(key=lambda i:i['created'], reverse=True)   # sorting for list of dict
    jcontext = {"jtemplate": {}}
    for i in jstring:
      if nsearch == None or nsearch in i['text']:
        created_index = i['created'][:10]       # cuts date only (first 10 characters)

        if not created_index in jcontext['jtemplate']:
          jcontext['jtemplate'][created_index] = []   # creates new list for date
        jcontext['jtemplate'][created_index].append(i)  # adds news to existing list

  return render(request, 'news/news.html', context=jcontext)


class CreateNews(View):
  def get(self, request):
    return render(request, 'news/create.html')
  def post(self, request):
    print(request.POST.get('title'))
    with open(settings.NEWS_JSON_PATH) as jf:
      jstring = json.load(jf)
    new_news = {}
    new_news['created'] = str(datetime.datetime.now())[:19]
    new_news['text'] = request.POST.get('text')
    new_news['title'] = request.POST.get('title')
    new_news['link'] = 222
    jstring.append(new_news)
    with open(settings.NEWS_JSON_PATH, "w") as jf:
      json.dump(jstring, jf)
    return redirect('/news')
