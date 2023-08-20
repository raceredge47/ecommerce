from django.db import models

# Create your models here.
class Product(models.Model):
    """
    Create model in MySql database with constraints.
    """
    Name = models.CharField(max_length=250)
    Description = models.CharField(max_length=250)
    Image = models.ImageField(upload_to='Product_Image/', default='')
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Stock = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)
