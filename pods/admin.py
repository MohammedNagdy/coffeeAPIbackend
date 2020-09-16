from django.contrib import admin
from .models import (LargeCoffeePod,SmallCoffeePod,EspressoCoffeePod)
from .model_list import MODELS_LIST

# add the models for the admin use

for model in MODELS_LIST:
	admin.site.register(model)

