from django.db import models


class Round(models.Model):
    round_number = models.CharField(max_length=20)
    round_picture = models.FileField()

    def __str__(self):
        return self.round_number


class Video(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    video_file = models.FileField()
    video_name = models.CharField(max_length=2000)

    def __str__(self):
        return self.video_name