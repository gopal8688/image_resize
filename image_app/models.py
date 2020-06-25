from django.db import models
import os
from PIL import Image


class Image_upload(models.Model):
    image = models.ImageField()

    def save(self):
        super().save()
        ima = Image.open(self.image.path)
        height, width = ima.size
        if height > 300 and width > 300:
            ima.thumbnail((200, 200), Image.ANTIALIAS)
            ima.save(self.image.path)

    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)
    #     width, height = img.size
    #     if img.height > 300 and img.width > 300:
    #         n_img = (300, 300)
    #         img.thumbnail(n_img,img.A)
    #         img.save(self.image.path)
    #
    # if 100 <= width <= 300 and 100 <= height <= 300:
    #     img.save()
    #     data = {
    #         'status': 'success',
    #         'message': 'Uploaded'
    #     }
    # elif width > 300 and height > 300:
    #     img.save()
    #     data = {
    #         'status': 'success',
    #         'message': 'Uploaded'
    #     }
