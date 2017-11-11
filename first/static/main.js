if (curr_username){
    var sock = new WebSocket("ws://" + window.location.host + "/")
    // sock.onmessage = function(e){console.log(e.data)}
    // sock.onmessage = function(e){console.log("got msg"); recvmsg(e);};
    sock.onmessage = recvmsg;
}

function updateScroll(){
    var element = document.getElementById("current-msgs");
    element.scrollTop = element.scrollHeight;
}

function sendmsg(){
    var friends = document.getElementById('friends');
    to_user = friends.getElementsByTagName('a')[0];
    if (!to_user){
        alert('first choose the user');
        return;
    }
    to_user = to_user.id;
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
    updateScroll();
    msg = {
        'type': 'sendmsg',
        'to_user': to_user,
        'text': text
    };
    sock.send(JSON.stringify(msg));
}

function recvmsg(e){
    console.log("Inside recvmsg");
    // console.log(e);
    data = JSON.parse(e.data);
    from_user = data.from_user;
    // console.log(data);
    if (data['type']=='get_all_msgs'){
        html = '';
        curr_msgs = document.getElementById('current-msgs');
        for (y in data['msgs']){
            x = data['msgs'][y]
            // console.log(x);
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
        // console.log(data['msgs'])
        updateScroll();
    }
    else if(data['type']=='sendmsg'){
        from_user = data['from_user'];
        from_user_name = data['from_user_name']
        text = data['text'];
        // console.log(text);
        var friend = document.getElementById(from_user);
        // console.log(friend);
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
            msg = {'type': 'exists', 'username': search_val};
            
            from_user = search_val;
            html = "<a href='#' class='collection-item' id='"+ from_user +"'" +
                  "onclick='loadConversation(\""+ from_user +"\")'>"+from_user+"</a>";
            var friends = document.getElementById('friends');
            friends.innerHTML = html + friends.innerHTML;
            curr_msgs = document.getElementById('current-msgs');
            curr_msgs.innerHTML = '';
            // loadConversation(from_user)
        }
        current_user = document.getElementById('current-user');
        current_user = current_user.getElementsByTagName('h4')[0];
        current_user.innerHTML = search_val;
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
    current_user = document.getElementById('current-user');
    current_user = current_user.getElementsByTagName('h4')[0];
    current_user.innerHTML = username;
}

// Create a webscoket

$(window).load(function() {
    console.log("inside initialize");
    var friends = document.getElementById('friends');
    first_friend = friends.getElementsByTagName('a')[0];
    if(!first_friend) return;
    username = first_friend.id;
    current_user = document.getElementById('current-user');
    current_user = current_user.getElementsByTagName('h4')[0];
    current_user.innerHTML = username;
    msg = {'type': 'get_all_msgs', 'user': username};
    msg = JSON.stringify(msg);
    setTimeout(function(){console.log("seding message"); sock.send(msg);}, 1000);
    // sock.send(msg);
   // initialize();
});

