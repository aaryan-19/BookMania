function Login() {
    email = document.getElementById('loginform').elements.item(0).value;
    password = document.getElementById('loginform').elements.item(1).value;

    url = window.location.href;

    var form = {
        'email': email,
        'password': password,
        'url': url
    };

    $.ajax({
        url: "/login",
        type: "POST",
        data: form,
        success: function (response) {
            html_response = JSON.parse(response).response
            url = JSON.parse(response).url

            if (url.length == 0){
                alert("Wrong Credentials");
            }
            $("body").html(html_response);

            window.location.href = url;
        
        }
    });
}

function signup() {
    FullName = document.getElementById('signupform').elements.item(0).value;
    email = document.getElementById('signupform').elements.item(1).value;
    username = document.getElementById('signupform').elements.item(2).value;
    password = document.getElementById('signupform').elements.item(3).value;

    var form = {
        'FullName': FullName,
        'email': email,
        'username': username,
        'password': password
    };

    $.ajax({
        url: "/create",
        type: "POST",
        data: form,
        success: function (response) {
            html_response = JSON.parse(response).response
            url = JSON.parse(response).url

            if (url.length == 0){
                alert("Same Email exist");
            }
            $("body").html(html_response);

            window.location.href = url;
        
        }

    });

}

function payment() {
    noOfElements = document.getElementById('payment-form').elements.length;
    coins = document.getElementById('payment-form').elements.item(1).value;
    var form = {
        'coins': coins
    };

    $.ajax({
        url: "/payment",
        type: "POST",
        data: form,
        success: function (response) {
            html_response = JSON.parse(response).response

            url = JSON.parse(response).url
            $("body").html(html_response);
            window.location.href = url;
        }
    });
}

function BuyBook(book_id, bookName){

    var form = {
        'BookName': bookName,
        'Book_id': book_id
    };
    $.ajax({
        url: "/buyBook",
        type: "POST",
        data: form,
        success: function (response) {

            html_response = JSON.parse(response).response

            url = JSON.parse(response).url
            console.log(url);
            if (url.length == 0){
                alert("Not Enough coins");
            }
            else{
                $("body").html(html_response);

                window.location.href = url;
            }

        }
    });
    
}

function readBook(book_id){

    var form = {
        'bookId' : book_id
    };

    
    $.ajax({
        url: "/book",
        type: "POST",
        data: form,
        success: function (response) {
            
            html_response = JSON.parse(response).response
            $("body").html(html_response);
            url = JSON.parse(response).url

        }
    });
}

function logout(){

    $.ajax({
        url: "/logout",
        type: "POST",
        success: function (response) {

            html_response = JSON.parse(response).response
            user_id = JSON.parse(response).user_id
 
            url = JSON.parse(response).url
            $("body").html(html_response);
            window.location.href = url;
        }
    });
}

function userDetails(){

    $.ajax({
        url: "/userDetails",
        type: "POST",
        success: function (response) {
            html_response = JSON.parse(response).response

            url = JSON.parse(response).url
            
            $("body").html(html_response);
  
        }
    });
}

function changePassword(){

    newPassword = document.getElementById("new-password").value;
    reType = document.getElementById("conf-new-password").value;
    compare = newPassword === reType;
    
    if (!compare){
        alert("Password Doesn't Match");
        return;
    }
    else{
        var form = {
            'newPassword' : newPassword
        };
    
        
        $.ajax({
            url: "/changePass",
            type: "POST",
            data: form,
            success: function (response) {
                
                html_response = JSON.parse(response).response

                $("body").html(html_response);
                url = JSON.parse(response).url

                window.location.href = url;
            }
        });
    }
}

function completeBook(book_id){

    var form = {
        'bookId' : book_id
    };

    
    $.ajax({
        url: "/completeBook",
        type: "POST",
        data: form,
        success: function (response) {
            
            html_response = JSON.parse(response).response
 
            $("body").html(html_response);
            url = JSON.parse(response).url
  
            $("body").html(html_response);
            window.location.href = url;
        }
    });
}