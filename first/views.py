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
def home_view(request):
    #c = RequestContext(request, {})
    c = {}
    c.update(csrf(request))
    return render(request, 'first/home.html', c)

#@csrf_protect
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
            return render(request, "first/home.html", {'empty_fields':False, 'wrong_input':False}.update(csrf(request)))
        else:
            return render(request, 'first/home.html', {'empty_fields':False, 'wrong_input':1}.update(csrf(request)))

    else:
        return HttpResponseRedirect(reverse("home_url"))

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse("home_url"))

#  @login_required
#  class AddMessageView(View):
#
#      @method_decorator(login_required)
#      def dispatch(self, request, *args, **kwargs):
#          return super(AddMessageView, self).dispatch(request, *args, **kwargs)
#
#      def post(self, request, *args, **kwargs):
#          new_msg = Message()
#          new_msg.from_user = request.user
#          try:
#              to_user = User.objects.get(id=request.POST['to'])
#          except:
#              response = {'success':False, msg:'To user does not exist'}
#              return JsonResponse(response)
#          new_msg.to_user = to_user
#
#          new_msg.save()
#          return JsonResponse({'success':True, msg:"message successfully sent"})


def get_chat(request):
    return render(request, "first/chatting.html")