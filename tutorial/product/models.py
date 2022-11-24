from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    stripe_product_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  # cents
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='product/static/product', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
