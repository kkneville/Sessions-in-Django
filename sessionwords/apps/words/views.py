# Still not working:
# 1 - for some reason, color and style persist between entries
# 2 - unable to clear session data with clear button/reset Function
# 3 - unable to leave "large" unselected, but still not showing large font size for new entries.




# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import *

def index(request):
    if "entries" not in request.session :
        request.session['entries'] = []
    entries = request.session['entries']
    context = {
        "entries": entries
    }
    return render(request, "words/index.html", context)

def add(request):

    date = strftime("%m-%d-%Y", gmtime())
    time = strftime("%H:%M:%S", gmtime())
    if len(request.POST['word']) < 1 :
        return redirect('/')
    else :
        word = request.POST['word']
    style = request.POST['style']
    if 'color' not in request.POST :
        color = "black;"
    else:
        color = request.POST['color']
    if request.POST['large'] == True :
        large = "30px"
    else :
        large = "12px"

    entry = {
        "date": date,
        "time": time,
        "word": word,
        "style": style,
        "color": color,
        "large": large,
    }

    entries = request.session['entries']
    entries.insert(0,entry)
    request.session['entries'] = entries
    print request.session['entries']

    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')






# def result(request):
#     date = request.session['date']
#     time = request.session['time']
#     word = request.session['word']
#     style = request.session['style']
#     color = request.session['color']
#     large = request.session['large']
#
#     entry = {
#         "date": date,
#         "time": time,
#         "word": word,
#         "style": style,
#         "color": color,
#         "large": large,
#     }
#
#     entries = []
#     entries.insert(0, entry)
#
#     context = {
#         "entries": entries
#     }
#     print context
#     print context['entries']
#
#     return render(request, "words/result.html", context)
