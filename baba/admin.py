from django.contrib import admin
from .models import UserProfile, Task, TaskTag
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Task)
admin.site.register(TaskTag)