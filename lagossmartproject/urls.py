from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/iot', include('iot.urls')),
    path('api/', include('meters.urls')),
    path('', include('frontend.urls')),
]