from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'person'
        ordering = ['-first_name']
    
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField(null=True, blank=True)
    exist_qty = models.IntegerField()
    moshakhast = models.JSONField(default=dict)

    def __str__(self) -> str:
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.user.first_name


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    qty = models.IntegerField()

    def __str__(self) -> str:
        return f"kharid {self.user.first_name}"