from time import time
from django.contrib.auth.models import AbstractUser


from django.db import models


class User(AbstractUser):
    pass



class Category(models.Model):
    class CategoryChoice(models.TextChoices):
        TOY = 'Toy'
        ELECTRONIC = 'Electronic'
        FURNITURE = 'Furniture'
        CLOTHING = 'Clothing'
        KITCHEN = 'Kitchen'
        
    title = models.CharField(max_length=20, choices=CategoryChoice.choices)

    def __str__(self):
        return f"{self.title}"
    


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sort')
    description = models.TextField()
    starting_price = models.FloatField()
    url = models.URLField(max_length=500)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='item', null=True)
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    

    def __str__(self):
        return f"{self.comment}"



class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watch")
    
    
    def __str__(self):
        return f"{self.pk}:{self.user}/{self.listing}"



class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bid_price = models.FloatField()
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    
    def __str__(self):
        return f"{self.bid_price}"

