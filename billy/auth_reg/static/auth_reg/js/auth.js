$(document).ready(function(){
    $(".auth").click(function(){
        var csrf_token =$("[name='csrfmiddlewaretoken']").val();
        var name = $("#name").val();
        var password = $("#password").val();

        $.ajax({
            url:"/auth/",
            type:"POST",
            data:{name:name,
                password:password,
                csrfmiddlewaretoken:csrf_token
            },

            success: function(response) {
                console.log(name)
            }
        })
    })
})