from django.db import models
from django.utils import timezone

#Model for posting the files
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="user_docs", null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
