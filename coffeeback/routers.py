# create a url for each model
from rest_framework import routers
from .urlrouters import URL_ROUTERS as urls
from coffee.viewsets import (LargeCoffeeMachineViewSet,SmallCoffeeMachineViewSet,EspressoCoffeeMachineViewSet)
from pods.viewsets import (LargeCoffeePodViewSet,SmallCoffeePodViewSet,EspressoCoffeePodViewSet)

router = routers.DefaultRouter()

for key, val in zip(urls.keys(), urls.values()):
	router.register(key, val)

