#consumers.py
from channels.auth import (
    channel_session_user, 
    channel_session_user_from_http, 
    http_session_user,
    channel_session,
)

#  @channel_session_user
@channel_session_user_from_http
def ws_echo(message):
    # print message.user.username
    print message
    print dir(message)
    print message.user
    message.reply_channel.send({
        'text': "You said: " + message.user.username+ "1" + message.content['text'],
    })
