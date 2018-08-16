from django.db import models


class Product(models.Model):
    short_title = models.CharField(max_length = 50, null = True)
    title = models.CharField(max_length = 120)
    slug = models.SlugField(blank = True, unique = True, null = True)
    short_description = models.TextField()
    description = models.TextField(blank = True)
    price = models.DecimalField(decimal_places = 0, max_digits = 7, default = 0)
    image = models.ImageField(upload_to = "products/img/", null = True, blank = True)
    add_image = models.ImageField(upload_to = "products/img/", null = True, blank = True)
    manual = models.FileField(upload_to = "products/manual/", null = True, blank = True)
    driver = models.FileField(upload_to = "products/driver/", null = True, blank = True)
    specifications = models.TextField()
    completeness = models.TextField()
    new = models.BooleanField(default=False)
    discount = models.DecimalField(max_digits = 2, decimal_places = 0, default = 0)

    def __str__(self):
        if self.short_title:
            return self.short_title
        return self.title
