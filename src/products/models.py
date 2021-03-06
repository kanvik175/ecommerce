from django.db import models
from django.urls import reverse

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length = 32)
    parent_category = models.ForeignKey('self', null = True, blank = True)


    def __str__(self):
        if self.name:
            return self.name

class Product(models.Model):
    short_title = models.CharField(max_length = 50, null = True)
    title = models.CharField(max_length = 120)
    slug = models.SlugField(unique = True, null = True)
    category = models.ForeignKey(Category, null = True)
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

    def get_absolute_url(self):
        return reverse("detail", kwargs = {"slug" : self.slug})

    def __str__(self):
        if self.short_title:
            return self.short_title
        return self.title
