from django.db import models
from django.urls import reverse
from cuentas.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name']),]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug])


class Product(models.Model):
    TALLA_CHOICES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
    ]
    COLOR_CHOICES = [
        ('negro', 'negro'),
        ('blanco', 'blanco'),
        ('gris', 'gris'),
    ]
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    talla = models.CharField(choices=TALLA_CHOICES,max_length=2)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id, self.slug])


class favoritos(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    producto = models.ForeignKey(Product,on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)

class Comentarios(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    producto = models.ForeignKey(Product,on_delete=models.CASCADE)
    review = models.CharField(max_length=255)
    creacion = models.DateTimeField(auto_now_add=True)