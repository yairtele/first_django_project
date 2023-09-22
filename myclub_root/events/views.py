from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import date
import calendar
from calendar import HTMLCalendar
from .models import Event
from .forms import VenueForm

def index(request, year=date.today().year, month=date.today().month):
    t = date.today()
    month = int(month)#date.strftime(t, '%b')
    year = int(year)
    if year < 2000 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month]
    title = "MyClub Event Calendar - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)

    announcements = [
        {
            'date': '9-23-2023',
            'announcement': "Club Registrations Open"
        },
        {
            'date': '9-28-2023',
            'announcement': "Joe Smith Elected New Club President"
        }
    ]

    #return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal))
    return render(request,
        'events/calendar_base.html',
        {'title': title, 'cal': cal, 'announcements': announcements}
    )

def all_events(request):
    event_list = Event.objects.all()
    return render(request,
        'events/event_list.html',
        {'event_list': event_list}
    )

def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue/?submitted=True')
    else:
        form = VenueForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 
        'events/add_venue.html', 
        {'form': form, 'submitted': submitted}
        )