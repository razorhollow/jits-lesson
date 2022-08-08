from django.db import models
from django.urls import reverse

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
  ('WU', 'Warmup'),
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

  def __str__(self):
    return self.name

  def thumbnail(self):
    return self.video.split('=')[1]

  def get_absolute_url(self):
    return reverse('technique_detail', kwargs={'technique_id': self.id})
