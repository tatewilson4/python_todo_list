from django.db import models
from django.urls import reverse

# Create your models here.

class Todo(models.Model):
    item = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('item_edit', kwargs={'pk': self.pk})
