from django.db import models

# the product type models

# o COFFEE_MACHINE_LARGE
class LargeCoffeeMachine(models.Model):
	large_machine = models.CharField(max_length=50, default='')
	flavor = models.CharField(max_length=50)
	is_waterline_compatible = models.BooleanField()


# o COFFEE_MACHINE_SMALL
class SmallCoffeeMachine(models.Model):
	small_machine = models.CharField(max_length=50, default='')
	flavor = models.CharField(max_length=50)
	is_waterline_compatible = models.BooleanField()


# o ESPRESSO_MACHINE
class EspressoCoffeeMachine(models.Model):
	espresso_machine = models.CharField(max_length=50, default='')
	flavor = models.CharField(max_length=50)
	is_waterline_compatible = models.BooleanField()


