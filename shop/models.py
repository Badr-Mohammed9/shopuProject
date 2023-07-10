from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200, default="user@email.com")

    def __str__(self):
        return str(self.user)


class Item(models.Model):
    CATEGORY_CHOICES = (
        ("Electronics", "Electronics"),
        ("Fashion", "Fashion"),
        # ("Home and Garden", "Home and Garden"),
        ("Sports and Outdoors", "Sports and Outdoors"),
        # ("Beauty and Health", "Beauty and Health"),
        ("Toys and Games", "Toys and Games"),
    )
    """
    Item model representing products on an e-commerce platform.
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owned_items",
        default=User.objects.first().id,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=50)
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, default="Uncategorized"
    )
    users = models.ManyToManyField(User, blank=True, related_name="interested_items")
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        """
        Returns a string representation of the Item model.
        """
        return self.name
