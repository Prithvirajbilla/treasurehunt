from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect
from open_facebook.api import OpenFacebook, FacebookAuthorization
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from problems.models import *

def view_prob(request):
	p = Problem.objects.get(pk=1)
	return render(request,"question.html",{"problem":p})