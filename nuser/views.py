from django.contrib.auth.models import User
from django.http import Http404
from django.http import HttpResponseForbidden
from nuser.models import UserProfile, FoundPerson
from nuser.forms import FoundPersonForm
from nuser.serializers import UserSerializer, FoundPersonSerializer
from django.shortcuts import render_to_response,get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import permissions
from rest_framework import status
from django.http import JsonResponse

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
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseNotAllowed


@api_view(('POST',))
def signin(request):
	phone = request.POST["username"]
	password = request.POST["password"]
	print phone, password
	list_data={}
	user = authenticate(username=phone, password=password)
	if user:
		list_data['is_user']="Yes"
	else:
		list_data['is_user']="No"
	list_data['error']='None'
	print list_data
	return Response(json.dumps(list_data))

def register_confirm(request, activation_key):  

    print "yoyo l"
    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

    if user_profile.key_expires < timezone.now():
        return HttpResponse("unable to confirm")
    user = user_profile.user
    user.is_active = True
    user.save()
    return HttpResponse("account verified")

class UserList(APIView):
	
    def post(self, request, format=None):
        """
        curl -H "Content-Type: application/json" -X POST -d '{"username":phonenumber,"password":password,"name":name,"email":email}' http://192.168.56.74:8001/signupuser/
        """
    	serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            user=serializer.save()
            user.set_password(user.password)
            user.is_active=False
            user.save()
            email=user.email
            username=user.username
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]            
            activation_key = hashlib.sha1(salt+email).hexdigest()            
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            user2=User.objects.get(username=username)
            new_profile = UserProfile(user=user2, activation_key=activation_key, key_expires=key_expires)
            #profile = profile_form.save(commit=False)
            new_profile.save()
            email_subject = 'Account confirmation'
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://192.168.56.74:8001/confirm/%s/" % (email, activation_key)
            send_mail(email_subject, email_body, 'email.chakshu@gmail.com',
                [email], fail_silently=False)
            print email_body
            registered = True
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def SaveFoundPerson(request):
    saved=False
    print "aa"
    if request.method=="POST":
        print "aaya post me"
        foundPersonForm = FoundPersonForm(request.POST, request.FILES)
        if foundPersonForm.is_valid():
            foundperson = FoundPerson()
            print "yoyo"
            foundperson.name = foundPersonForm.cleaned_data["name"]
            foundperson.location = foundPersonForm.cleaned_data["location"]
            foundperson.picture = foundPersonForm.cleaned_data["picture"]
            foundperson.save()
            all_data = FoundPerson.objects.all()
            saved = True
    else:
        foundPersonForm=FoundPersonForm()

    return render(request, 'saved.html', locals())

class PhotoList(APIView):
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)
    print "ada"
    def post(self, request, format=None):
        serializer = FoundPersonSerializer(data=request.DATA)
        print request.POST["name"]
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print serializer.errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(('GET',))
def getcontribution(request):
    try :
        uploaded_by=request.GET['uploaded_by']
        all_contributions=FoundPerson.objects.all().filter(uploaded_by=uploaded_by)
        contribution_items = {}
        counter=1
        for contribution in all_contributions:
            Cname=contribution.name
            Clocation=contribution.location
            Cpicture=contribution.picture.url
            # print Cname, Clocation, Cpicture
            item = {"Cname":Cname, "Clocation":Clocation,"Cpicture":Cpicture,"Cpicture":Cpicture}
            contribution_items[counter]=item
            counter+=1
        return JsonResponse(contribution_items)
    except :
        contribution_items = {}
        return JsonResponse(contribution_items)

