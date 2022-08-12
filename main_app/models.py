from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

CATEGORIES = (
  ('CG', 'Closed Guard'),
  ('BG', 'Butterfly  Guard'),
  ('SG', 'Spider Guard'),
  ('LG', 'Lasso Guard'),
  ('DLR', 'De La Riva Guard'),
  ('HGB', 'Half Guard Bottom'),
  ('HGT', 'Half Guard Top'),
  ('SCB', 'Side Control Bottom'),
  ('SCT', 'Side Control Top'),
  ('MT', 'Mount Top'),
  ('ME', 'Mount Escape'),
  ('BC', 'Back Control'),
  ('BE', 'Back Escape'),
  ('KOB', 'Knee On Belly'),
  ('NS', 'North South'),
  ('GP', 'Guard Pass'),
  ('GR', 'Guard Retention'),
  ('TD', 'Takedown'),
  ('OT', 'Other')
)



class Technique(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=500)
  counter = models.IntegerField(default=0)
  video = models.URLField(blank=True)
  category = models.CharField(
    max_length=4,
    choices=CATEGORIES,
    default=CATEGORIES[0][0]
  )
  modified = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def thumbnail(self):
    if len(self.video) and '=' in self.video:
      return self.video.split('=')[1]

  def get_absolute_url(self):
    return reverse('technique_detail', kwargs={'technique_id': self.id})

  class Meta:
    ordering = ['category', 'modified']

class Category_Index(models.Model):
  index = models.IntegerField(default=0)

  def __str__(self):
    return f'{self.index}'

  def get_current_category(self):
    return CATEGORIES[self.index][1]

