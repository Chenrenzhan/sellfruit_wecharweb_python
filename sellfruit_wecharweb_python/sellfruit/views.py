#!/usr/bin/python
#encoding=utf-8

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def index(request):
    #return HttpResponse(get_template('index.html'))
    return render_to_response('index.html')

def order(request):
    return render_to_response('order.html')

def comment(request):
    return render_to_response('comment.html')