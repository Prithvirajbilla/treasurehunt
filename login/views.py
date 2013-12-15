# Create your views here.
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect,Http404
from open_facebook.api import OpenFacebook, FacebookAuthorization
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from login.models import *
from problems.models import *

def index(request):
	if request.user.is_authenticated():
		user = request.user
		return HttpResponseRedirect("/treasure")
	else:
		if request.method == 'GET':
			l=Level.objects.all()[:10]
			return render(request,"main.html",{'u':l})
		elif request.method == 'POST':
			return render(request,"main.html")

def next(request):
	if request.user.is_authenticated and request.user.id != None:
		print request.user.id
		l = Level.objects.get(user_id=request.user.id)
		level_id = l.level_id
		user = FacebookProfile.objects.get(user=FacebookCustomUser(pk=request.user.id))
		problem = Problem.objects.get(pk=level_id+1)
		if 'p' in request.GET:
			p = request.GET['p']
			if p=='error':
				return render(request,"question.html",{"problem":problem,"user":user,'error':True,
					"logged_in":True})
			elif p=='success':
				return render(request,"question.html",{"problem":problem,"user":user,'success':True
					,"logged_in":True})
			else:
				return render(request,"question.html",{"problem":problem,"user":user,"logged_in":True})
		else:
			return render(request,"question.html",{"problem":problem,"user":user,"logged_in":True})
	else:
		return HttpResponseRedirect("/")

def register_next(request):
	if request.user.is_authenticated and request.user.id != None:
		try:
			l = Level(user_id=FacebookCustomUser.objects.get(pk=request.user.id),level_id=0,
				profile_id=FacebookProfile.objects.get(user=FacebookCustomUser(pk=request.user.id)))
			l.save()
		except Exception, e:
			raise Http404
		fb = request.user.get_offline_graph(request)
		message = "I'm an Adventurer, Looking for a treasure. come join me."
		fb.set('me/feed', message=message,url="http://treasurehunt.stab-iitb.org/")

		return HttpResponseRedirect("/treasure")


def myscore(request,uid):
	try:
		uid = int(uid)
		print uid
		l = Level.objects.get(user_id=FacebookCustomUser(id=uid))
		print l.user_id
	except Exception,e:
		raise Http404
	if request.user.is_authenticated and request.user.id != None:
		fb = request.user.get_offline_graph(request)
		message = "I'm an Adventurer, Looking for a treasure. come join me."
		fb.set('me/feed', message=message,url="http://treasurehunt.stab-iitb.org/")
		user = FacebookProfile.objects.get(user=FacebookCustomUser(pk=request.user.id))
		return render(request,"myscore.html",{"level":l,"logged_in":True,'user':user})
	else:
		raise Http404
