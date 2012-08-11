#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from events.models import *
from operator import attrgetter


# Create your views here.

def events(request, event_name):
    event_name = event_name.replace('-', ' ')
    if event_name == 'sampark/' :
        return sampark(request)
    event = Event.objects.get(title=event_name)
    initial_updates = Update.objects.filter(category = 'Update')
    updates = sorted(initial_updates, key=attrgetter('id'), reverse=True)
    initial_announcements = Update.objects.filter(category = 'Announcement')
    announcements = sorted(initial_announcements, key=attrgetter('id'), reverse=True)
    tab_set = event.tab_set.all()
    return render_to_response('events/events.html', locals(), context_instance=RequestContext(request))


def tabs(request, event_name, tab_name):
    event_name = event_name.replace('-', ' ')
    tab_name = tab_name.replace('-', ' ')
    event = Event.objects.get(title=event_name)
    tab_set = event.tab_set.all()
    tab = tab_set.get(title=tab_name)
    file_set = tab.tabfile_set.all()
    return render_to_response('events/tabs.html', locals(), context_instance=RequestContext(request))

def sampark(request):
#    if path:
#        assert False
#        return HttpResponseRedirect(settings.SITE_URL+path)
    bengaluruevents = []
    hyderabadevents = []
    puneevents = []
    event = Event.objects.all()
    city_set = ['Bengaluru', 'Hyderabad', 'Pune']
    for e in event:
        if e.title.split('_')[0] == 'B':
            bengaluruevents.append(e)
        if e.title.split('_')[0] == 'H':
            hyderabadevents.append(e)
        if e.title.split('_')[0] == 'P':
            puneevents.append(e)
    return render_to_response('events/sampark_home.html', locals(), context_instance=RequestContext(request))
        
