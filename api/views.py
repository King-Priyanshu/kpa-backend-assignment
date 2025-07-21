from django.shortcuts import render

from rest_framework import generics
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer

# POST and GET /api/forms/wheel-specifications
class WheelSpecificationListCreateView(generics.ListCreateAPIView):
    queryset = WheelSpecification.objects.all()
    serializer_class = WheelSpecificationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Optional filtering logic (if any filters are passed in query params)
        form_number = self.request.query_params.get('formNumber')
        if form_number:
            queryset = queryset.filter(form_number=form_number)

        return queryset
