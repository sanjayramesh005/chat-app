from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.http import (
    JsonResponse
)
from django.core import serializers

from second.models import Message

class AddMessageView(View):
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AddMessageView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        new_msg = Message()
        new_msg.from_user = request.user
        try:
            to_user = User.objects.get(username=request.POST['to'])
        except:
            response = {'success':False, 'msg':'To user does not exist'}
            return JsonResponse(response)
        new_msg.to_user = to_user
        new_msg.text = request.POST['text']
        new_msg.save()
        return JsonResponse({'success':True, 'msg':"message successfully sent"})

class GetAllMessages(View):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(GetAllMessages, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        user = request.user
        username = request.GET['user']
        try:
            other_user = User.objects.get(username=username)
        except:
            response = {'success':False, 'msg': 'User does not exist'}
            return JsonResponse(response)
        
        msgs = list(Message.objects.filter(from_user=user, to_user=other_user))
        msgs_tmp = list(Message.objects.filter(from_user=other_user, to_user=user))
        msgs+=msgs_tmp
        msgs.sort(key=lambda x: x.time, reverse=True)
        all_msgs = [msg.to_dict() for msg in msgs]
        return JsonResponse(all_msgs, safe=False)

class GetAllUsers(View):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(GetAllUsers, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        user = request.user
        msgs = Message.objects.filter(from_user=user)
        users = [msg.to_user for msg in msgs]
        msgs = Message.objects.filter(to_user=user)
        users_tmp = [msg.from_user for msg in msgs]
        users+=users_tmp
        users = list(set(users))
        #  users = serializers.serialize('json', users)
        users = [{"username":user.username, "name":
                  user.first_name+" "+user.last_name} for user in users]
        return JsonResponse(users, safe=False)
