from django.db import models

# pods product type models

# o COFFEE_POD_LARGE
class LargeCoffeePod(models.Model):
	large_pod = models.CharField(max_length=50, default='')
	packet_size = models.CharField(max_length=50)
	flavor = models.CharField(max_length=50)


# o COFFEE_POD_SMALL
class SmallCoffeePod(models.Model):
	small_pod = models.CharField(max_length=50, default='')
	packet_size = models.CharField(max_length=50)
	flavor = models.CharField(max_length=50)


# o ESPRESSO_POD
class EspressoCoffeePod(models.Model):
	espresso_pod = models.CharField(max_length=50, default='')
	packet_size = models.CharField(max_length=50)
	flavor = models.CharField(max_length=50)



