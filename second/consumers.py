#consumers.py
from channels.auth import (
    channel_session_user, 
    channel_session_user_from_http, 
    channel_session, 
)
from channels import Group
import json
from django.contrib.auth.models import User

from second.models import Message

@channel_session_user_from_http
def ws_connect(message):
    http_user = True
    print "connect", message.user.username
    Group(message.user.username).add(message.reply_channel)
    message.reply_channel.send({
        'accept': True,
    })

@channel_session_user
def ws_receive(message):
    print message.content, message.user
    msg = json.loads(message.content['text'])
    new_msg = Message(text=msg['text'], from_user=message.user)
    to_user = User.objects.get(username=msg['to_user'])
    new_msg.to_user = to_user
    new_msg.save()
    Group(to_user.username).send({
        'from_user': message.user.username, 
        'text': msg['text'],
    })
    #  message.reply_channel.send({
    #      'text': "You said: " + message.user.username+ " " + message.content['text'],
    #  })
