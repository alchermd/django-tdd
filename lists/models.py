from django.db import models


class Task(models.Model):
    title = models.TextField(default='')
    list = models.ForeignKey('List', on_delete=models.CASCADE, default=None)


class List(models.Model):
    pass
