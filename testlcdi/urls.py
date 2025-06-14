from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('dashboard', include('dashboard.urls')),
    path('peta/', include('peta.urls')),
    path('api/', include('api.urls')),
]
