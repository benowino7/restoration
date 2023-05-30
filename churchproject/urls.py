# type:ignore
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('churchapp.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django_registration.backends.activation.urls')),
]
