from django.db import models

class ProductEntry(models.Model):
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


    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.TextField()
    category = models.CharField(max_length=15,choices=category_choices)
    # image = to be added later
    conditions = models.DecimalField
    brand = models.CharField(max_length=100)
    gender = models.CharField(max_length=6,choices=gender_choices)

    # @property
    # to be added later