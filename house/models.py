import os 
import uuid

from django.db import models
from django.utils.deconstruct import deconstructible

@deconstructible
class GenerateProfileImagePath(object):

    def __int__(self):
        pass

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path = f"media/house/{instance.id}/images/"
        name = f"main.{ext}"
        return os.path.join(path, name)
    
house_image_path = GenerateProfileImagePath()

class House(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to=house_image_path, blank=True, null=True)
    created_on = models.DateField(auto_now_add=True)
    description = models.TextField()
    manager = models.OneToOneField('users.Profile', on_delete=models.SET_NULL, blank=True, null=True, related_name='managed_house')
    points = models.IntegerField(default=0)
    completed_tasks_count = models.IntegerField(default=0)
    noncompleted_tasks_count = models.IntegerField(default=0)