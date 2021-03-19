from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    stock_count = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="", blank=True)

    # Please add a field called "sku".
    # - This is a unique code for each product.
    # - It is a string of maximum 20 characters long.
    # - Make sure that the field label in the admin says "stock keeping unit"
    #   instead of just "sku".
    #
    # Then, try to create and run the migration for this.