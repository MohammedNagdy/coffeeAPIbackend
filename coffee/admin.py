from django.contrib import admin
from .models import (LargeCoffeeMachine,SmallCoffeeMachine,EspressoCoffeeMachine)
from .model_list import MODELS_LIST


# username: momo123 pw: momo123
# register the models for the admin access
for model in MODELS_LIST:
	admin.site.register(model)