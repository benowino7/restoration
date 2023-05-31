# type:ignore
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UpdateUserForm,UpdateProfileForm,ClientSignUpForm,AdminSignUpForm,ReviewForm,CermonForm,EventForm,ImpactCategoryForm,ImpactForm,PaymentForm,GalleryForm,FaqForm,TeamForm
from .models import User,Profile,Review,Cermon,ImpactCategory,Impact,Event,PaymentMethod,Gallery,Team,Faq
from django.views.generic import CreateView
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage




def home(request):
    reviews = Review.objects.all()
    cermons = Cermon.objects.all()
    excluded_categories = ['economical', 'social','technology']  # Names of categories to exclude
    remaining = ImpactCategory.objects.exclude(name__in=excluded_categories)
    for remained in remaining:
        impact_items = Impact.objects.filter(category = remained)

    s =ImpactCategory.objects.filter(name='social').first()
    t =ImpactCategory.objects.filter(name='technology').first()
    e =ImpactCategory.objects.filter(name='economical').first()
    social = Impact.objects.filter(category = s).all()
    technology = Impact.objects.filter(category = t).all()
    economical = Impact.objects.filter(category = e).all()
    donation_methods = PaymentMethod.objects.all()
    ministry = Gallery.objects.filter(category ="ministry").all()
    outreach = Gallery.objects.filter(category ="outreach").all()
    donation = Gallery.objects.filter(category ="donation").all()
    faqs = Faq.objects.all()
    members = Team.objects.all()
    context = {
        "reviews": reviews,
        "cermons":cermons,
        "impacts":impact_items,
        "donation_methods":donation_methods,
        "social":social,
        "technology":technology,
        "economical":economical,
        "donation":donation,
        "outreach":outreach,
        "ministry":ministry,
        "faqs":faqs,
        "members":members,
               }

    return render(request, 'index.html',context)

def Events(request):
    products_db = Event.objects.all()
    paginator = Paginator(products_db, 3)
    page = request.GET.get('page')
    count = paginator.get_page(page)
    total_pages = count.paginator.num_pages
    try:
        events = paginator.get_page(page)
    except PageNotAnInteger:
       events = paginator.get_page(1)
    except EmptyPage:
        events = paginator.get_page(paginator.num_pages)
    context= {
        "events": events,
        "total_pages": total_pages,
        "count":count,
    }
    return render(request, 'blog.html',context)

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
            messages.success(request, 'Sermon added successfully!')
            return redirect('churchapp:home')
    else:
        form = CermonForm()
        messages.error(request, 'Correct the error below')

    return render(request, 'cermon_form.html', { "form":form})

@login_required(login_url='login')
def event_form(request):
    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event added successfully!')
            return redirect('churchapp:home')
    else:
        form = EventForm()
        messages.error(request, 'Correct the error below')

    return render(request, 'cermon_form.html', { "form":form})

@login_required(login_url='login')
def impact_category_form(request):
    if request.method == 'POST':
        form = ImpactCategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('churchapp:home')
    else:
        form = ImpactCategoryForm()
        messages.error(request, 'Correct the error below')

    return render(request, 'cermon_form.html', { "form":form})

@login_required(login_url='login')
def impact_form(request):
    if request.method == 'POST':
        form = ImpactForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Impact item added successfully!')
            return redirect('churchapp:home')
    else:
        form = ImpactForm()
        messages.error(request, 'Correct the error below')

    return render(request, 'cermon_form.html', { "form":form})

@login_required(login_url='login')
def payment_method_form(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Payment method added successfully!')
            return redirect('churchapp:home')
    else:
        form = PaymentForm()
        messages.error(request, 'Correct the error below')

    return render(request, 'cermon_form.html', { "form":form})

@login_required(login_url='login')
def gallery_form(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gallery Image added successfully!')
            return redirect('churchapp:home')
    else:
        form = GalleryForm()
        messages.error(request, 'Correct the error below')

    return render(request, 'cermon_form.html', { "form":form})


@login_required(login_url='login')
def faq_form(request):
    if request.method == 'POST':
        form = FaqForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Faqs added successfully!')
            return redirect('churchapp:home')
    else:
        form =FaqForm()
        messages.error(request, 'Correct the error below')

    return render(request, 'cermon_form.html', { "form":form})


@login_required(login_url='login')
def team_form(request):
    if request.method == 'POST':
        form = TeamForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member added successfully!')
            return redirect('churchapp:home')
    else:
        form =TeamForm()
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