from __future__ import unicode_literals

from django.db import models
from mongoengine import *
from mongoengine import connect
connect('ceshi', host='127.0.0.1', port=27017)

# ORM
class ArtiInfo(Document):
    # des = StringField()
    # scores = StringField()
    # tages = ListField(StringField)
    title = StringField()
    area = StringField()
    url = StringField()
    price = StringField()
    user = StringField()

    meta = {'collection': 'item_infoU'}
