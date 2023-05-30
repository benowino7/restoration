# type:ignore
from django.urls import path,include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from .views import home,Events,AdminSignUpView,ClientSignUpView,review_form,cermon_form,event_form,impact_form,impact_category_form,payment_method_form

app_name = 'churchapp'


urlpatterns = [
    path('',home,name="home"),
    path('events',Events,name="events"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('accounts/signup/admin/3567/', AdminSignUpView.as_view(), name='admin_signup'),
    path('accounts/signup/client/', ClientSignUpView.as_view(), name='client_signup'),
    path('add/testimony/form',review_form,name='review_form'),
    path('add/sermon/form',cermon_form,name='cermon_form'),
    path('add/event/form',event_form,name='event_form'),
    path('add/impact/category/form',impact_category_form,name='impact_category_form'),
    path('add/impact/form',impact_form,name='impact_form'),
    path('add/payment/method/form',payment_method_form,name='payment_form'),



    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)