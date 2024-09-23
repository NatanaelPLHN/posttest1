from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from KatalogLaptop.models.laptop import Laptop  


class Rating(models.Model):
    id_rating = models.BigAutoField(primary_key=True)
    review = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  
    recommended = models.BooleanField(default=True)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='ratings')  

    def __str__(self):
        return self.review
