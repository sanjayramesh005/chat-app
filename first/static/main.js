// Create a webscoket
if (curr_username){
    var sock = new WebSocket("ws://" + window.location.host + "/")
    // sock.onmessage = function(e){console.log(e.data)}
    sock.onmessage = function(e){recvmsg(e);};
}

$(window).load(function() {
    var friends = document.getElementById('friends');
    username = friends.getElementsByTagName('a')[0].id;
    msg = {'type': 'get_all_msgs', 'user': username};
    msg = JSON.stringify(msg);
    setTimeout(function(){sock.send(msg);}, 1000);
    // sock.send(msg);
   // initialize();
});

function sendmsg(){
    el = document.getElementById('msg-input');
    text = el.value;
    el.value = '';
    if(!text){
        return;
    }
    html_tmp = '<div class="card teal darken-1 to-msg">' +
    '<div class="card-content white-text">' + text +
    '</div></div>';
    var curr_msgs = document.getElementById('current-msgs');
    curr_msgs.innerHTML = curr_msgs.innerHTML + html_tmp;
    var friends = document.getElementById('friends');
    to_user = friends.getElementsByTagName('a')[0].id;
    msg = {
        'type': 'sendmsg',
        'to_user': to_user,
        'text': text
    };
    sock.send(JSON.stringify(msg));
}

function recvmsg(e){
    console.log(e);
    data = JSON.parse(e.data);
    from_user = data.from_user;
    console.log(data);
    if (data['type']=='get_all_msgs'){
        html = '';
        curr_msgs = document.getElementById('current-msgs');
        for (y in data['msgs']){
            x = data['msgs'][y]
            console.log(x);
            if(x['from_username']==curr_username){
				html_tmp = '<div class="card teal darken-1 to-msg">' +
				'<div class="card-content white-text">' + x['text'] +
				'</div></div>';
                html+=html_tmp;
            }
            else{
				html_tmp = '<div class="card red  accent-1 from-msg">' +
				'<div class="card-content">' + x['text'] +
				'</div></div>';
                html+=html_tmp;
            }
        }
        curr_msgs.innerHTML = html;
        console.log(data['msgs'])
    }
    else if(data['type']=='sendmsg'){
        from_user = data['from_user'];
        from_user_name = data['from_user_name']
        text = data['text'];
        console.log(text);
        var friend = document.getElementById(from_user);
        console.log(friend);
        if(friend){
            friend.parentNode.removeChild(friend);
            html = "<a href='#' class='collection-item' id='"+ from_user +"'" +
                  "onclick='loadConversation(\""+ from_user +"\")'>"+from_user+"</a>";
            var friends = document.getElementById('friends');
            friends.innerHTML = html + friends.innerHTML;
            loadConversation(from_user)
        }
        else{
            html = "<a href='#' class='collection-item' id='"+ from_user +"'" +
                  "onclick='loadConversation(\""+ from_user +"\")'>"+from_user+"</a>";
            var friends = document.getElementById('friends');
            friends.innerHTML = html + friends.innerHTML;
            loadConversation(from_user)
        }
    } 
}

function newUserChat(){
    search_val = document.getElementById('search-input').value;
    document.getElementById('search-input').value = '';
    if(search_val){
        friend = document.getElementById(search_val);
        if(friend){
            from_user = search_val;
            friend.parentNode.removeChild(friend);
            html = "<a href='#' class='collection-item' id='"+ from_user +"'" +
                  "onclick='loadConversation(\""+ from_user +"\")'>"+from_user+"</a>";
            var friends = document.getElementById('friends');
            friends.innerHTML = html + friends.innerHTML;
            loadConversation(from_user)
        }
        else{
            from_user = search_val;
            html = "<a href='#' class='collection-item' id='"+ from_user +"'" +
                  "onclick='loadConversation(\""+ from_user +"\")'>"+from_user+"</a>";
            var friends = document.getElementById('friends');
            friends.innerHTML = html + friends.innerHTML;
            curr_msgs = document.getElementById('current-msgs');
            curr_msgs.innerHTML = '';
            // loadConversation(from_user)
        }
    }
}

function loadConversation(username){
    msg = {'type': 'get_all_msgs', 'user': username};
    msg = JSON.stringify(msg);
    sock.send(msg);
}

function clickUser(username){
    html = "<a href='#' class='collection-item' id='"+ username +"'" +
          "onclick='clickUser(\""+ username +"\")'>"+username+"</a>";
    var friends = document.getElementById('friends');
    friend = document.getElementById(username)
    friend.parentNode.removeChild(friend);
    friends.innerHTML = html + friends.innerHTML;
    loadConversation(username);
}
