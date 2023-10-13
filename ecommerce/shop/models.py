from django.db import models

class Category(models.Model):
    cname = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='shop/category',null=True,blank=True)

    def __str__(self):
        return self.cname

class Product(models.Model):
    pname = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='shop/product',null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pname
