# type:ignore
from django.urls import path,include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from .views import home,Events,AdminSignUpView,ClientSignUpView


app_name = 'churchapp'


urlpatterns = [
    path('',home,name="home"),
    path('events',Events,name="events"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('accounts/signup/admin/3567/', AdminSignUpView.as_view(), name='admin_signup'),
    path('accounts/signup/client/', ClientSignUpView.as_view(), name='client_signup'),

    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)