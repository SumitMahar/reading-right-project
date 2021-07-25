from django import forms 

from .models import Grocery

class GroceryForm(forms.ModelForm):
    
    class Meta:
        model = Grocery
        fields = ['item_name', 'item_quantity', 'item_status']


 