from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Avoid conflict with default 'auth.User.groups'
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Avoid conflict with default 'auth.User.user_permissions'
        blank=True,
    )

class Recipe(models.Model):
   
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/')
    average_rating = models.FloatField(default=0)

    def __str__(self):
        # Return the name of the current instance
        return self.name

class Rating(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not (1 <= self.rating <= 5):
            raise ValidationError('Rating must be between 1 and 5')

    def __str__(self):
        # Return the name of the recipe associated with the rating
        return self.recipe.name

    



