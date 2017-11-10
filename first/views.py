from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import UserForm
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
from second.models import Message

from forms import UserForm
# @csrf_protect
def register_view(request):
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            email_exists = User.objects.filter(email=form.cleaned_data['email']).exists()
            if email_exists:
                return render(request, 'first/register.html', {'form':form, 'email_exists':True, 'fail':True})
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email, password)
            user.last_name = last_name
            user.first_name = first_name
            user.save()
            user=authenticate(username=username, password=password)
            login(request, user)
            url = reverse('home_url')
            return HttpResponseRedirect(url)
        else:
            return render(request, 'first/register.html', {'form':form, 'fail':True})
    else:
        form = UserForm()
        return render(request, 'first/register.html', {'form':form, 'fail':False})

#@csrf_protect

def get_all_users(user):
    msgs = Message.objects.filter(from_user=user)
    users = [msg.to_user for msg in msgs]
    msgs = Message.objects.filter(to_user=user)
    users_tmp = [msg.from_user for msg in msgs]
    users+=users_tmp
    users = list(set(users))
    msgs = list()
    for u in users:
        msg = list(Message.objects.filter(from_user=u, to_user=user))
        msg_tmp = list(Message.objects.filter(from_user=user, to_user=u))
        msg+=msg_tmp
        msg.sort(key=lambda x: x.time, reverse=True)
        msgs.append(msg[0])

    print msgs
    msgs.sort(key=lambda x: x.time, reverse=True)
    users = [msg.from_user if msg.from_user.username!=user.username else msg.to_user for
            msg in msgs]
    users = [{"username":u.username, "name":
              u.first_name+" "+u.last_name} for u in users]
    print users
    return users

def home_view(request):
    #c = RequestContext(request, {})
    print request.user
    print request.user.is_authenticated()
    if request.user.is_authenticated():
        users = get_all_users(request.user)
        return render(request, 'first/chatting.html', {'users':users,
                                                       'curr_user':request.user})
    else:
        c = {}
        c.update(csrf(request))
        return render(request, 'first/home.html', c)

#  @login_required
def login_view(request):
    if request.method=="POST":
        try:
            username=request.POST['username']
        except KeyError:
            return render(request, "first/home.html", {'empty_fields':True, 'wrong_input':False}.update(csrf(request)))
        try:
            password=request.POST['password']
        except KeyError:
            return render(request, 'first/home.html', {'empty_fields':True, 'wrong_input':False}.update(csrf(request)))

        user=authenticate(username=username, password=password)
        # user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print request.user.username
            #  return render(request, "first/home.html", {'empty_fields':False, 'wrong_input':False}.update(csrf(request)))
            return HttpResponseRedirect(reverse("home_url"))
        else:
            return HttpResponseRedirect(reverse("home_url"))
            #  return render(request, 'first/home.html', {'empty_fields':False, 'wrong_input':1}.update(csrf(request)))

    else:
        return HttpResponseRedirect(reverse("home_url"))

def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
    return HttpResponseRedirect(reverse("home_url"))

def get_chat(request):
    return render(request, "first/chatting.html")
