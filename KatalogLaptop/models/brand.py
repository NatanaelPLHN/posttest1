# from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
# # from KatalogLaptop.models.brand import Brand

# class Brand(models.Model):
#     id_brand = models.PositiveBigIntegerField(unique=True, validators=[MinValueValidator(1)])
#     brand_name = models.CharField(max_length=50)
#     desc = models.CharField(max_length=100)
#     country = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.brand_name