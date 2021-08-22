document.addEventListener('DOMContentLoaded', function(){ 
    let add_user_elem = document.getElementsByClassName("delete_user");
    
    Array.prototype.forEach.call(add_user_elem, function(element) {
        element.addEventListener('click', function() {
            let user_id = this.parentNode.querySelector("li").innerText
            let xhr = new XMLHttpRequest();
            xhr.open("POST", "/users", true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.send(JSON.stringify({"id": user_id}));
            
            xhr.onreadystatechange=function(){
                if (xhr.readyState==4 && xhr.status==200){
                    document.location.reload();
                }
            }

        });
    });
});