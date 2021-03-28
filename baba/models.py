from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, default='1',blank=False)
   dob = models.DateField(blank=False)
   created_on = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return str(self.user) # TODO

class TaskTag(models.Model):
    title = models.CharField(max_length=20, blank=False)
    created_by = models.ForeignKey(UserProfile,on_delete=models.DO_NOTHING )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title # TODO

class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title # TODO

