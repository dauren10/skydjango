from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from django.http import HttpResponse, HttpResponseNotFound,Http404,HttpResponseBadRequest
from bs4 import BeautifulSoup
import requests
@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        try:
            method=request.GET['method']
            if method == 'ping':
                return HttpResponseNotFound()
            else:
                return HttpResponseBadRequest()
        except:
            return HttpResponseBadRequest()
    else:
        return Response({"message": "Hello, world!"})

@api_view(['GET'])
def parse(request):
    r = requests.get('https://www.skydns.ru')
    html=r.text
    soup = BeautifulSoup(html)
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    return HttpResponse(text)