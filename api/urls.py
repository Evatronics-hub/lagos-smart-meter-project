from django.urls import path, include

from .views import (
    MeterAPIView, MeterRetrieveAPIView
)

urlpatterns = [
    path('meters', MeterAPIView.as_view()),
    path('meters/<int:pk>', MeterRetrieveAPIView.as_view()),
]