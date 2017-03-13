from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("hello world")

def sss(request,test_id,api_id):
    return HttpResponse("hello sss %s %s" % (test_id,api_id))