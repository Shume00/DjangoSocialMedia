from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.PROTECT)
    blockedUser = models.ManyToManyField(User, default='', null=True, blank=True, related_name='blocked_users')

    def __str__(self):
        return self.firstName


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    files = models.FileField()
    date = models.DateField()
    lastChange = models.DateField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField()
    user = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE)
    blogPost = models.ForeignKey(BlogPost, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


