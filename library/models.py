from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class categoryModel(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')])
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'category'
    
class subCategoryModel(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(categoryModel, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'subcategory'
        
class authorsModel(models.Model):
    fullname = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=datetime.now)
    birth_country = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photos/Authors", blank=True)
    
    def __str__(self) -> str:
        return self.fullname
    
    class Meta:
        db_table = 'bookauthors'
        
class booksModel(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='Books/')
    category = models.ForeignKey(categoryModel, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(subCategoryModel, on_delete=models.CASCADE)
    author = models.ForeignKey(authorsModel, on_delete=models.CASCADE)
    file = models.FileField(upload_to='audio/', null=True, blank=True)
    views_count = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'books'


class CustomUser(AbstractUser):
    user_picture = models.ImageField(upload_to='user_pictures/', blank=True, null=True)

    def __str__(self):
        return self.username 


class commentsModel(models.Model):
    book = models.ForeignKey(booksModel, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    
    def __str__(self) -> str:
        return str(self.user)
    
    class Meta:
        db_table = 'comments'

        