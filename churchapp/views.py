# type:ignore
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from rest_framework import permissions
from rest_framework.response import Response
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import filters
from .forms import UpdateUserForm,UpdateProfileForm,ClientSignUpForm,AdminSignUpForm
from .models import User,Profile
from django.utils.crypto import get_random_string
from django.views.generic import CreateView



def home(request):
    return render(request, 'index.html')

def Events(request):
    return render(request, 'blog.html')

class AdminSignUpView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'registration/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'registration/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')
    

# @login_required(login_url='login')
# def profile(request, username):
#     return render(request, 'profile.html')

# @login_required(login_url='login')
# def edit_profile(request, username):
#     user = User.objects.get(username=username)
#     Profile.objects.get_or_create(user=request.user)
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         prof_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         if user_form.is_valid() and prof_form.is_valid():
#             user_form.save()
#             prof_form.save()
#             # messages.success(request, 'Your profile was updated successfully!')
#             return redirect('kiddoApp:profile', user.username)
#     else:
#         # messages.error(request, 'Please correct the error below!')
#         user_form = UpdateUserForm(instance=request.user)
#         prof_form = UpdateProfileForm(instance=request.user.profile)
    
#     return render(request, 'editprofile.html', {'user_form': user_form, 'prof_form': prof_form})


# def home(request):
#     if request.user.is_authenticated:
#         Profile.objects.get_or_create(user=request.user)
#     else:
# 		# if not, create an anonymous user and log them in
#         username = get_random_string(length=32)
#         u = User(username=username, first_name='Anonymous', last_name='User')
#         u.set_unusable_password()
#         u.save()
#         u.username = u.id
#         u.save()
#         Profile.objects.get_or_create(user=u)
#         authenticate(user=u)
#         login(request, u)
    

#     return render(request, 'index.html')