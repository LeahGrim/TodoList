from django.db import models
# import user
from django.contrib.auth.models import User 

# Create your models here.
class Task(models.Model):
    # create a foreign key model to manage everything related to user in our app
    # if our user is deleted, data is deleted 
    user= models.ForeignKey(User, on_delete= models.CASCADE, null= True, blank=True)
    title = models.CharField(max_length=200, null=True)
    # TextField automatically alerts django that there will be lots of text, no need to specify max length
    description = models.TextField(null=True, blank=True)
    # creates the checklist with an ability to complete the task created, when it is completed user will switch it to True
    complete = models.BooleanField(default=False)
    #when a new task is created, the date and time will automatically be assigned to the task
    created = models.DateTimeField(auto_now_add=True)

    def__str__(self):
        return self.title

    Class Meta:
        # completed tasks will be ordered down
        ordering = ['complete'] 