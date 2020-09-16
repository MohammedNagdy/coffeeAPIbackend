# serializers file to send JSON response
from rest_framework import serializers
from .models import (LargeCoffeeMachine,SmallCoffeeMachine,EspressoCoffeeMachine)


class LargeCoffeeMachineSerializer(serializers.ModelSerializer):
	class Meta:
		model = LargeCoffeeMachine
		fields = "__all__"


class SmallCoffeeMachineSerializer(serializers.ModelSerializer):
	class Meta:
		model = SmallCoffeeMachine
		fields = "__all__"


class EspressoCoffeeMachineSerializer(serializers.ModelSerializer):
	class Meta:
		model = EspressoCoffeeMachine
		fields = "__all__"
