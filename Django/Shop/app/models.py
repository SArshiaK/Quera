from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



# class ProductManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(int(OrderItem.quantity) >= 1)
class ProductManager(models.Manager):
    # Product.objects.filter(stock__gte=0)
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(stock__gte=1)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    available = ProductManager()
    objects = ProductManager()

    def __str__(self):
        return self.name


class Order(models.Model):
    address = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self):
        return '{}'.format(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

