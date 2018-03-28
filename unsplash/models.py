from django.db import models
from mongoengine import *
# Create your models here.


connect('unsplash', host='127.0.0.1', port=27017)


class ImageLinks(Document):
    author = StringField()
    url = StringField()
    time = StringField()
    h = StringField()
    w = StringField()

    meta = {'collection': 'alls'}


for image in ImageLinks.objects[:3]:
    print(image.author, image.url, image.time, image.h, image.w)
