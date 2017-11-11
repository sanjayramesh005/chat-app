#consumers.py
from channels.auth import (
    channel_session_user, 
    channel_session_user_from_http, 
    channel_session, 
)
from channels import Group
import json
from django.contrib.auth.models import User
from channels.asgi import get_channel_layer

from second.models import Message

@channel_session_user_from_http
def ws_connect(message):
    http_user = True
    print "connect", message.user.username
    Group(message.user.username).add(message.reply_channel)
    channel_layer = get_channel_layer()
    ch_group_list = channel_layer.group_channels(message.user.username)
    print ch_group_list

    message.reply_channel.send({
        'accept': True,
    })

def get_all_msgs(user, username):
    #  user = request.user
    #  username = request.GET['user']
    try:
        other_user = User.objects.get(username=username)
    except:
        response = {'success':False, 'msg': 'User does not exist'}
        return response
    
    msgs = list(Message.objects.filter(from_user=user, to_user=other_user))
    msgs_tmp = list(Message.objects.filter(from_user=other_user, to_user=user))
    msgs+=msgs_tmp
    msgs = list(set(msgs))
    msgs.sort(key=lambda x: x.time)
    all_msgs = [msg.to_dict() for msg in msgs]
    #  return JsonResponse(all_msgs, safe=False)
    return all_msgs

@channel_session_user
def ws_receive(message):
    #  print message.content, message.user
    msg = json.loads(message.content['text'])
    
    if msg['type']=='sendmsg':
        new_msg = Message(text=msg['text'], from_user=message.user)
        to_user = User.objects.get(username=msg['to_user'])
        new_msg.to_user = to_user
        new_msg.save()
        
        response = {
            'type': 'sendmsg', 
            'from_user': message.user.username,
            'from_user_name': message.user.first_name+" "+message.user.last_name,
            'text': msg['text']
        }
        if to_user!=message.user:
            Group(to_user.username).send({
                #  'from_user': message.user.username,
                'text': json.dumps(response),
            })

    elif msg['type']=='get_all_msgs':
        all_msgs = get_all_msgs(message.user, msg['user'])
        #  print all_msgs
        response = {'type': 'get_all_msgs', 'msgs': all_msgs}
        Group(message.user.username).send({
            'text': json.dumps(response)
        })


@channel_session_user
def ws_disconnect(message):
    print "in disconnect"
    Group(message.user.username).discard(message.reply_channel)
    
