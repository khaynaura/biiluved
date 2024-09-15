import uuid
from django.db import models

class Product(models.Model):
    category_choices = [
        ("clothing", "Clothing"),
        ("shoes", "Shoes"),
        ("bags", "Bags"),
        ("acc", "Accessories"),
        ("others", "Others")
    ]
    gender_choices = [
        ("women", "Women"),
        ("men", "Men"),
        ("unisex", "Unisex")
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=15,choices=category_choices)
    # image = to be added later
    conditions = models.CharField(max_length=100, default= "no information")
    brand = models.CharField(max_length=100)
    gender = models.CharField(max_length=6,choices=gender_choices)

    # @property
    # to be added later