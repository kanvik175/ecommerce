from django.db import models

class Product(models.Model):
    title = models.CharField(max_length = 120)
    short_description = models.TextField()
    description = models.TextField()
    price = models.DecimalField(decimal_places = 2, max_digits = 20, default = 0)
    image = models.ImageField(null = True, blank = True)
    manual = models.FileField(null = True, blank = True)
    driver = models.FileField(null = True, blank = True)
    specifications = models.TextField()
    completeness = models.TextField()
