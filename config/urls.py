from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from gym import views as gym_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/registro/', gym_views.registro, name='registro'),
    path('auth/', include('django.contrib.auth.urls')),
    path('gym/', include('gym.urls')),
    path('', RedirectView.as_view(url='gym/', permanent=False)),
]
