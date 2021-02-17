from django.db import models

class BagType(models.Model):
    type_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'bag_types'

class BagModel(models.Model):
    model_name     = models.CharField(max_length=100)
    video          = models.URLField()
    bag_type       = models.ForeignKey('BagType', on_delete=models.CASCADE, related_name='bag_models')

    class Meta:
        db_table = 'bag_models'

class Product(models.Model):
    model_number = models.CharField(max_length=100)
    price        = models.DecimalField(max_digits=15, decimal_places=2)
    description  = models.TextField()
    bag_model    = models.ForeignKey('BagModel', on_delete=models.CASCADE, related_name='products')
    color        = models.ForeignKey('Color', on_delete=models.CASCADE, related_name='products')
    size         = models.ForeignKey('Size', on_delete=models.CASCADE, related_name='products')

    class Meta:
        db_table = 'products'

class Color(models.Model):
    color_name    = models.CharField(max_length=100)

    class Meta:
        db_table = 'colors'

class Size(models.Model):
    size_name    = models.CharField(max_length=100)

    class Meta:
        db_table = 'sizes'

class Image(models.Model):
    image_url = models.URLField()
    product   = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')

    class Meta:
        db_table = 'images'

class Recommendation(models.Model):
    product   = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='recommendations')
    bag_model = models.ForeignKey('BagModel', on_delete=models.CASCADE, related_name='recommendations')
