from django.db import models

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    mark = models.CharField(max_length=100, blank=True, default='')
    datafile = models.FileField()
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)