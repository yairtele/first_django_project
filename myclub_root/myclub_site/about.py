from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

def about(request):
    return render(request, 
        'about/about.html', 
        )