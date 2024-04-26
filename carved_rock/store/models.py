from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    stock_count = models.IntegerField(null=True,
                                      help_text="How many items are currently in stock")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="", blank=True)
    sku = models.CharField(verbose_name="Stock Keeping Unit", max_length=20, unique=True)

    class Meta:
        ordering = ['price']

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return str(self.image)


class Category(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField('Product', related_name="categories")

    def __str__(self):
        return self.name
