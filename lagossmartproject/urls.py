from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(title='API')

urlpatterns = [
    path('api/auth/', include('users.urls')),
    path('api/', include('meters.urls')),
    path('api/iot', include('iot.urls')),
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
]