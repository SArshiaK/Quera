from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'stock']

        
    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get("price")
        description = cleaned_data.get("description")
        if int(price) > 1000:
            raise ValidationError("Product is too expensive")

        if len(description) <= 20:
            raise ValidationError("Product must have a good description")
    
    

