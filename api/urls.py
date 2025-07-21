from django.urls import path
from .views import WheelSpecificationListCreateView

urlpatterns = [
    path('forms/wheel-specifications', WheelSpecificationListCreateView.as_view()),
]
