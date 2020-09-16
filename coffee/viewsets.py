# view sets file to view the JSON data
from rest_framework import (viewsets, generics, filters )
from django_filters import rest_framework as filters
from .models import (LargeCoffeeMachine,SmallCoffeeMachine,EspressoCoffeeMachine)
from .serializers import (LargeCoffeeMachineSerializer,SmallCoffeeMachineSerializer,EspressoCoffeeMachineSerializer) 


class LargeCoffeeMachineViewSet(viewsets.ModelViewSet, filters.FilterSet):
	queryset = LargeCoffeeMachine.objects.all()
	serializer_class = LargeCoffeeMachineSerializer
	filterset_fields = "__all__"


class SmallCoffeeMachineViewSet(viewsets.ModelViewSet, filters.FilterSet):
	queryset = SmallCoffeeMachine.objects.all()
	serializer_class = SmallCoffeeMachineSerializer
	filterset_fields = "__all__"


class EspressoCoffeeMachineViewSet(viewsets.ModelViewSet, filters.FilterSet):
	queryset = EspressoCoffeeMachine.objects.all()
	serializer_class = EspressoCoffeeMachineSerializer
	filterset_fields = "__all__"
