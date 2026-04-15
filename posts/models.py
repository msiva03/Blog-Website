from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=50)
    post_content = models.TextField(default="")
    published_date =models.DateField(auto_now=True)

    # def __str__(self):
    #     return self.post_title

class User_details(models.Model):
    name = models.CharField()
    mail=models.EmailField()
    contact_number = models.IntegerField()
    bio= models.TextField()