from django.db import models
from multipleimgproject import settings

class ImgFile(models.Model):
    media = models.FileField(upload_to='images')



class Posts(models.Model):
    texts = models.TextField()
    file_content = models.ManyToManyField(ImgFile, related_name='file_content', blank=True, null=True)
    

    class Meta:

        verbose_name_plural = ('Posts')
