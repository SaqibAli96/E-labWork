from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    users = models.OneToOneField(User,on_delete=models.CASCADE)

     #Use model extension
    user_type = models.CharField(max_length=6)

    def __str__(self):
         return self.users.username

class Book(models.Model):
    book_name = models.CharField(max_length=50)
    uploaded_by = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    book_price = models.IntegerField(default=0)
    book_type = models.CharField(max_length=10)
    book_cover = models.ImageField(upload_to="book_images/",blank=True)
    book_description = models.TextField()
    book_category = models.CharField(max_length=30)
    book_file = models.FileField(upload_to="book/")
    upload_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.book_name)

class photo(models.Model):
    empty_cover = models.ImageField(upload_to = 'default/', null=True)
