from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import DetailView
from django.utils import timezone
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
import json
from datetime import datetime

#-------////----------INDEX--------////------------------# 

def index(request):
    return render (request, "aplicacion/index.html")

#-------////----------FIN INDEX--------////------------------# 

def staff(request):
    return render (request, "aplicacion/staff.html")


#-------////----------TURNOS--------////------------------# 

def turnos(request):
    return render (request, "aplicacion/turnos.html")

#-------////----------FIN TURNOS--------////------------------# 



#-------////----------ROBOTS.TXT--------////------------------#

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "",
        "Sitemap: https://juliaps.com.ar/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


