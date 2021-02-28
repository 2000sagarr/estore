from django.db import models
from datetime import datetime

# Create your models here.
class Products(models.Model):
    # choices
    brand_choices = (
        ('mufti' , 'Mufti'),
        ('park_avenue' , 'Park Avenue'),
        ('levis', "Levi's"),
        ('pepe_jeans','Pepe Jeans'),
        ('peter_england', 'Peter England'),
        ('biba', 'Biba'),
        ('flying_machine', 'Flying Machine'),
        ('raymond', 'Raymond'),
        ('max', 'Max'),
        ('adidas', 'Adidas'),
        ('nike', 'Nike'),
        ('saraa', 'Saraa'),

    )
    category_choices = (
        ('kids', 'Kids'),
        ('babies', 'Babies'),
        ('men', 'Men'),
        ('women', 'Women'),
        ('winter', 'Winter Cloths'),
    )

    gender_choices= (
        ('male', 'Male'), 
        ('female', 'Female'),
    )
    occasion_choices = (
        ('CASUAL', 'CASUAL'),
        ('formal', 'FORMAL'),
        ('CLUB_CASUAL', 'CLUB CASUAL'),
        ('saree', 'SAREE'),
        ('BUSINESS_CASUAL', 'BUSINESS CASUAL'),
        ('t-shirt', 'T-shirt'),
        ('regular' , 'Regular'),
    )
    material_choices = (
        ('cotton','Cotton'),
        ('silk','Silk'),
        ('linen', 'Linen'),
        ('wool', 'Wool'),
        ('leather', 'Leather'),
        ('nylon', 'Nylon'),
        ('velvet', 'Velvet'),
        ('denim', 'Denim'),

    )
    size_choices = (
        ('s','S'),
        ('m','M'),
        ('l','L'),
        ('xl','XL'),
        ('xxl','XXL'),
    )
    # feilds in db table
    name = models.CharField(max_length=200)
    description = models.TextField()
    brand = models.CharField(
        max_length=100,
        choices=brand_choices,
        )
    category = models.CharField(
        max_length=50,
        choices=category_choices,
        )
    gender = models.CharField(
        max_length=50,
        choices= gender_choices
        )
    occasion = models.CharField(
        max_length=50,
        blank= True,
        choices=occasion_choices
    )
    material = models.CharField(
        max_length= 50,
        choices=material_choices,
    )
    size = models.CharField(
        max_length=3,
        choices=size_choices,
    )
    color = models.CharField(max_length=50)
    photo = models.ImageField(upload_to = 'media/products/%Y/%m')    
    quantity = models.IntegerField()
    quanity_sell = models.IntegerField(default=0)
    price = models.FloatField()
    discount_percentage = models.FloatField()
    is_featured = models.BooleanField(default= False)
    created_date= models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.name
    
    