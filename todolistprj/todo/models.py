from django.db import models
# import user
from django.contrib.auth.models import User 

# Create your models here.
class Task(models.Model):
    # create a foreign key model to manage everything related to user in our app
    # if our user is deleted, data is deleted 
    user= models.ForeignKey(User, on_delete= models.CASCADE, null= True, blank=True)
    title =  models.CharField(max_length=200, null=True)
    # TextField automatically alerts django that there will be lots of text, no need to specify max length
    description = models.TextField(null=True, blank=True)