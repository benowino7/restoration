# type:ignore
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Admin,Client,User,Review,Cermon,ImpactCategory,Impact,Event,PaymentMethod,Gallery,Team,Faq
from django.db import transaction


class AdminSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        admin = Admin.objects.create(user=user)
        admin.save()
        return user

class ClientSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        client = Client.objects.create(user=user)
        client.save()
        return user

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'location', 'profile_pic')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('profile_pic','first_name','last_name','comment')

class CermonForm(forms.ModelForm):
    class Meta:
        model = Cermon
        fields = ('theme','description','reading','link','date','image')

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title','description','event_date','image')

class ImpactCategoryForm(forms.ModelForm):
    class Meta:
        model = ImpactCategory
        fields = ('name',)


class ImpactForm(forms.ModelForm):
    class Meta:
        model = Impact
        fields = ('title','description','category','image')

class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ('method','email','till','paybill','account')

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('category','image')


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name','rank','image')

class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ('question','answer')