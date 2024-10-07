from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "conditions", "category", "brand", "gender"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    
    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    def clean_conditions(self):
        conditions = self.cleaned_data["conditions"]
        return strip_tags(conditions)
    
    def clean_category(self):
        category = self.cleaned_data["category"]
        return strip_tags(category)
    
    def clean_brand(self):
        brand = self.cleaned_data["brand"]
        return strip_tags(brand)
    
    def clean_gender(self):
        gender = self.cleaned_data["gender"]
        return strip_tags(gender)



