from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('gym/', include('gym.urls')),
    path('', RedirectView.as_view(url='gym/', permanent=False)),
]
