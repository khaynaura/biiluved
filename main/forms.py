from django.forms import ModelForm
from main.models import Product

class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "conditions", "category", "brand", "gender"]

