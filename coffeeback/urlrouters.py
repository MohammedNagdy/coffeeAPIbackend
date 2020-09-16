# urls for each viewset
from coffee.viewsets import (LargeCoffeeMachineViewSet,SmallCoffeeMachineViewSet,EspressoCoffeeMachineViewSet)
from pods.viewsets import (LargeCoffeePodViewSet,SmallCoffeePodViewSet,EspressoCoffeePodViewSet)


URL_ROUTERS = {
	'large_machine': LargeCoffeeMachineViewSet,
	'small_machine': SmallCoffeeMachineViewSet,
	'espresso_machine': EspressoCoffeeMachineViewSet, 
	'large_pod': LargeCoffeePodViewSet, 
	'small_pod': SmallCoffeePodViewSet,
	'espresso_pod': EspressoCoffeePodViewSet,
}