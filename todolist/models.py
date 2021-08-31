from django.db import models

# Create your models here.
from django.utils import timezone
class ItemList(models.Model):
    title = models.CharField(max_length=250) # a varchar
    content = models.TextField(blank=True) # a text field 
    class Meta:
        verbose_name = ("Item")
        verbose_name_plural = ("Items")
    def __str__(self):
        return self.title #name to be shown when called