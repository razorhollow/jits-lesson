from django.db import models

class Technique(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=500)
  counter = models.IntegerField(default=0)
  video = models.URLField(blank=True)
  modified = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

  def thumbnail(self):
    return self.video.split('=')[1]
