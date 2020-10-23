from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from datetime import datetime

def index(request):
    return HttpResponse("Hello!")

def health(request):
    dateTimeObj = datetime.now()
    
    status = {
    "status": "OK",
    "version": "0.0.1",
    "uptime": str(dateTimeObj)
    }
    return JsonResponse(status)
    

# Create your views here.
