# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import *

def index(request):
    print request.session
    print '-'*20
    if "entries" not in request.session :
        request.session['entries'] = []
    entries = request.session['entries']
    context = {
        "entries": entries
    }
    print context
    return render(request, "words/index.html", context)

def add(request):

    date = strftime("%m-%d-%Y", gmtime())
    time = strftime("%H:%M:%S", gmtime())
    if len(request.POST['word']) < 1 :
        flash("Please enter a word")
        return redirect('/')
    else :
        word = request.POST['word']
    style = request.POST['style']
    #add conditional for no color selected
    color = request.POST['color']
    #add work on this conditional
    if request.POST['large'] == "True" :
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

    request.session['entries'].insert(0,entry)
    print request.session['entries']

    return redirect('/')

def reset(request):
    # session.request.pop()
    # incomplete
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
