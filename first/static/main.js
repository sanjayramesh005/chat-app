// Create a webscoket

var sock = new WebSocket("ws://" + window.location.host + "/")
sock.onmessage = function(e){console.log(e.data)}

function sendmsg(to_user, text){
    msg = {
        'to_user': to_user,
        'text': text
    };
    sock.send(JSON.stringify(msg));
}

function recvmsg(e){
    data = e.data;
    from_user = data.from_user;
    text = data.text;
    console.log(text);
}
