from django.db import models
from django.contrib.auth.models import User

import datetime

class Message(models.Model):
    from_user = models.ForeignKey(User, related_name='fromuser')
    to_user = models.ForeignKey(User)
    time = models.DateTimeField(default=datetime.datetime.now)
    text = models.TextField()

    def to_dict(self):
        response = dict()
        response['from_username'] = self.from_user.username
        #  response['from_user'] = self.from_user.firstname + " " +
        response['to_username'] = self.to_user.username
        response['time'] = str(self.time)
        response['text'] = self.text
        return response
