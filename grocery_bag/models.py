from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse



# Create your models here.
class Grocery(models.Model):
    '''
        Model for Grocery items
        item_name : str
        item_quantity : +int
        item_status : str
        date_added : DateTime obj
        owner = instance of User model
    '''
    # the first value in the tuple : script sees
    # second value : user sees
    CHOICES = [
                ('BOUGHT', 'BOUGHT'),
                ('PENDING', 'PENDING'),
                ('NOT-AVAILABLE', 'NOT AVAILABLE')
    ]

    item_name = models.CharField(max_length=150)
    item_quantity = models.PositiveIntegerField()
    item_status = models.CharField(
                    max_length=70, 
                    choices=CHOICES, 
                    default='PENDING')
    date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = 'Groceries'

    def get_absolute_url(self):
        return reverse("g_bag:home")
    

    # string representation of the model instance
    def __str__(self):
        return f"{self.item_name} ({self.item_status})"
