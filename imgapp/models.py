from django.db import models
from multipleimgproject import settings



class Posts(models.Model):
    texts = models.TextField()


class ImgFile(models.Model):
    media = models.FileField(upload_to='images')
    file_content = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True, blank=True)




    
    



