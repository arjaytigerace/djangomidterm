from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField('date published', auto_now_add=True)
    date_updated = models.DateTimeField('date updated', null=True, auto_now=True)
    content = models.TextField()
    #is_active = models.admin(is_active= True)

    def __str__(self):
        return 'Title: {}'.format(self.title)


class Comment(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return 'Comment: {}'.format(self.content)
