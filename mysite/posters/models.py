from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

# Create your models here.
class Poster(models.Model):
    name = models.CharField(max_length=255, blank=False)
    location = models.CharField(max_length=255, blank=False)
    start_date = models.DateField(blank=False)
    poster = ProcessedImageField(upload_to='avatars',
                                processors=[ResizeToFit(600,1000)],
                                format='JPEG',
                                options={'quality': 60})
    link = models.URLField()
