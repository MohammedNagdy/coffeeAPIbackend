# serializers file to send JSON response
from rest_framework import serializers
from .models import (LargeCoffeePod,SmallCoffeePod,EspressoCoffeePod)


class LargeCoffeePodSerializer(serializers.ModelSerializer):
	class Meta:
		model = LargeCoffeePod
		fields = "__all__"


class SmallCoffeePodSerializer(serializers.ModelSerializer):
	class Meta:
		model = SmallCoffeePod
		fields = "__all__"


class EspressoCoffeePodSerializer(serializers.ModelSerializer):
	class Meta:
		model = EspressoCoffeePod
		fields = "__all__"
