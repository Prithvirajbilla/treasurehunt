from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect,Http404
from open_facebook.api import OpenFacebook, FacebookAuthorization
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from problems.models import *
from login.models import *

def view_prob(request):
	p = Problem.objects.get(pk=1)
	return render(request,"question.html",{"problem":p})

def ans(request):
	if request.method == 'GET':
		if 'answer' in request.GET:
			ans = request.GET['answer']
			if request.user.is_authenticated and request.user.id != None:
				l = Level.objects.get(user_id=request.user)
				level_id = l.level_id+1;
				print level_id
				problem = Problem.objects.get(pk=level_id)
				return HttpResponse(problem.answer)
				if problem.answer == answer:
					l.level_id = l.level_id+1
					l.save()
					return HttpResponseRedirect("/treasure/?p=success")
				else:
					return HttpResponseRedirect("/treasure/?p=error")
			else:
				return HttpResponseRedirect("/")
		else:
			return HttpResponseRedirect("/")
	else:
		if 'answer' in request.POST:
			answer = request.POST['answer']
			if request.user.is_authenticated and request.user.id != None:
				l = Level.objects.get(user_id=request.user)
				level_id = l.level_id+1;
				print level_id
				problem = Problem.objects.get(pk=level_id)
				if problem.answer == answer:
					l.level_id = l.level_id+1
					l.save()
					return HttpResponseRedirect("/treasure/?p=success")
				else:
					return HttpResponseRedirect("/treasure/?p=error")
			else:
				return HttpResponseRedirect("/")
		raise Http404

def leaderboard(request):
	if 'p' in request.GET:
		p = request.GET['p']
		l=Level.objects.all()
		if request.user.is_authenticated and request.user.id != None:
			return render(request,"leaderboard.html",{"logged_in":True})
		else:
			return render(request,"leaderboard.html")

	l = Level.objects.all().order_by('-level_id')
	if request.user.is_authenticated and request.user.id != None:
		user = FacebookProfile.objects.get(user=FacebookCustomUser(pk=request.user.id))
		return render(request,"leaderboard.html",{'u':l,'value':0,"logged_in":True,"user":user})
	else:
		return render(request,"leaderboard.html",{'u':l,'value':0})

from django.contrib.auth import logout as django_logout

def logout(request):
    django_logout(request)
    return HttpResponseRedirect("/")

def help(request):
	h = Help.objects.all()
	if request.user.is_authenticated and request.user.id != None:
		user = FacebookProfile.objects.get(user=FacebookCustomUser(pk=request.user.id))
		return render(request,"help.html",{"h":h,"logged_in":True,"user":user})
	else:
		return render(request,"help.html",{"h":h})

def rules(request):
	h = Rules.objects.all()
	if request.user.is_authenticated and request.user.id != None:
		user = FacebookProfile.objects.get(user=FacebookCustomUser(pk=request.user.id))
		return render(request,"rules.html",{"h":h,"logged_in":True,"user":user})
	else:
		return render(request,"rules.html",{"h":h})

