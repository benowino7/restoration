# type:ignore
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import filters
from .forms import UpdateUserForm,UpdateProfileForm,ClientSignUpForm,AdminSignUpForm,ReviewForm,CermonForm
from .models import User,Profile,Review,Cermon
from django.views.generic import CreateView
from django.contrib import messages




def home(request):
    reviews = Review.objects.all()
    cermons = Cermon.objects.all()
    return render(request, 'index.html',{"reviews": reviews,"cermons":cermons})

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





@login_required(login_url='login')
def review_form(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'testimony was added successfully!')
            return redirect('churchapp:home')
    else:
        form = ReviewForm()
        messages.error(request, 'Correct the error below')

    return render(request, 'review_form.html', { "form":form})


@login_required(login_url='login')
def cermon_form(request):
    if request.method == 'POST':
        form = CermonForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'cermon was added successfully!')
            return redirect('churchapp:home')
    else:
        form = CermonForm()
        messages.error(request, 'Correct the error below')

    return render(request, 'cermon_form.html', { "form":form})
    

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