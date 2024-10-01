from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Laptop(models.Model):
    id_laptop = models.BigAutoField(primary_key=True)
    laptop_name = models.CharField(max_length=50)
    spec = models.CharField(max_length=100)
    price = models.IntegerField(validators=[MinValueValidator(10000)])
    total_rating = models.FloatField(default=0)  

    def __str__(self):
        return self.laptop_name
