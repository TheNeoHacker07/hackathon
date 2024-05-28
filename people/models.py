from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    name=models.CharField(max_length=13)
    surename=models.CharField(max_length=13)
    about=models.TextField()
    image=models.ImageField(upload_to='user_img',blank=True)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.email










