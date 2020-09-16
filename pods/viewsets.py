# view sets file to view the JSON data
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import (LargeCoffeePod,SmallCoffeePod,EspressoCoffeePod)
from .serializers import (LargeCoffeePodSerializer,SmallCoffeePodSerializer,EspressoCoffeePodSerializer) 


class LargeCoffeePodViewSet(viewsets.ModelViewSet):
	queryset = LargeCoffeePod.objects.all()
	serializer_class = LargeCoffeePodSerializer
	filterset_fields = "__all__"



class SmallCoffeePodViewSet(viewsets.ModelViewSet):
	queryset = SmallCoffeePod.objects.all()
	serializer_class = SmallCoffeePodSerializer
	filterset_fields = "__all__"



class EspressoCoffeePodViewSet(viewsets.ModelViewSet):
	queryset = EspressoCoffeePod.objects.all()
	serializer_class = EspressoCoffeePodSerializer
	filterset_fields = "__all__"
