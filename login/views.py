# Create your views here.
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect
from open_facebook.api import OpenFacebook, FacebookAuthorization
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from login.models import *
from problems.models import *

def index(request):
	if request.method == 'GET':
		return render(request,"main.html")
	elif request.method == 'POST':
		return render(request,"main.html")

def register_next(request):
	user = request.user.id
	# graph = user.get_offline_graph()
	l = Level.objects.get(user_id=FacebookCustomUser.objects.get(pk=1))
	level_id = l.level_id
	problem = Problem.objects.get(pk=level_id+1)
	return render(request,"questions.html",{"graph":problem.answer})

def next(request):
	l = Level(user_id=FacebookCustomUser.objects.get(pk=1),level_id=0)
	l.save()
	return HttpResponseRedirect("/treasure")

