from django.db import models

# Item Model
class Item(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200)
  content = models.CharField(max_length=200)
      
  def __str__(self):
    return self.title