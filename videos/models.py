from django.db import models
from django.core.urlresolvers import reverse
class video_type(models.Model):
    title = models.CharField(max_length=2000)
    picture = models.FileField()


    def get_absolute_url(self):
        return reverse('videos:detail', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.title

class video(models.Model):
    type=models.ForeignKey(video_type,on_delete=models.CASCADE)
    name = models.CharField(max_length=2000)
    file = models.FileField()

    def __str__(self):
        return self.name