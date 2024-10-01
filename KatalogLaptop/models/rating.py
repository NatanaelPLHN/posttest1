from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.db.models import Avg  # Import Avg for average calculation
from KatalogLaptop.models.laptop import Laptop


class Rating(models.Model):
    id_rating = models.BigAutoField(primary_key=True)
    review = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    recommended = models.BooleanField(default=True)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return self.review


# Signal to update total rating
@receiver(post_save, sender=Rating)
def update_total_rating_on_add(sender, instance, created, **kwargs):
    if created:
        laptop = instance.laptop
        # Recalculate average rating and scale to 0-10
        average_rating = laptop.ratings.aggregate(Avg('rating'))['rating__avg'] or 0
        laptop.total_rating = average_rating * 2  # Scale to 0-10
        laptop.save()


# Signal to update total rating on delete
@receiver(pre_delete, sender=Rating)
def update_total_rating_on_delete(sender, instance, **kwargs):
    laptop = instance.laptop
    # Recalculate average rating and scale to 0-10
    average_rating = laptop.ratings.aggregate(Avg('rating'))['rating__avg'] or 0
    laptop.total_rating = average_rating * 2  # Scale to 0-10
    laptop.save()
