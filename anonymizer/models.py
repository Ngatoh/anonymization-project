import os
from django.core.files import File
from django.db import models
from django.utils import timezone
from django.contrib import admin

#Model for posting the files
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    #published_date = models.DateTimeField(
            #blank=True, null=True)
    anonymized_file = models.FileField(null=True, blank=True)

    #def publish(self):        #self.published_date = timezone.now()

        #with open(filepath, 'rb') as fi:
             #self.anonymized_file = File(fi, name=os.path.basename(self.title))
             #FieldFile.save(self.title, fi)
             #f = open('/path/to/file')
             #self.license_file.save(new_name, File(f))
             #self.save()
    
    def __str__(self):
        return self.title
