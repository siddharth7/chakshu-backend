from django.contrib.auth.models import User
from django.http import Http404
from django.http import HttpResponseForbidden
from nuser.models import UserProfile
from django.shortcuts import render_to_response,get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

import hashlib
import random

from django.core import serializers
from django.core.mail import send_mail
from django.utils import timezone
import datetime

from django.core.context_processors import csrf
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.template import RequestContext  

from django.views.decorators.csrf import csrf_exempt
import json

from django.views.generic.base import View
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

def signin(request):
	phone=request.GET.get('phone')
	password=request.GET.get('password')
	print phone, password
	user = authenticate(username=phone, password=password)
	login(request, user)
	list_data={}
	list_data['error']='None'
	return list_data

