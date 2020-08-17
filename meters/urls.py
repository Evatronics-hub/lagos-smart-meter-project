from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from .api import (
    MeterAPIView, MeterRetrieveAPIView,
    MeterTypeAPIView, MeterTypeRetrieveAPIView

)

schema_view = get_schema_view(title='API')
docs_urls = include_docs_urls(title='API')

urlpatterns = [
    path('schema/', schema_view),
    path('docs/', docs_urls),
    path('meters', MeterAPIView.as_view()),
    path('meters/<int:pk>', MeterRetrieveAPIView.as_view()),
    path('metertypes', MeterTypeAPIView.as_view()),
    path('metertypes/<int:pk>', MeterTypeRetrieveAPIView.as_view()),
]