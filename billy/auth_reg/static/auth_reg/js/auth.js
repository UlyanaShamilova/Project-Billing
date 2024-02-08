$(document).ready(function(){
    $(".auth").click(function(){
        var csrf_token =$("[name='csrfmiddlewaretoken']").val();
        var name = $("#name").val();
        var password = $("#password").val();

        $.ajax({
            url:"",
            type:"POST",
            data:{
                username: name,
                password: password,
                csrfmiddlewaretoken: csrf_token
            },
            success: function(response) {
                console.log(name)
                $("#name").val("");
                $("#password").val("");
            }
        });
    });
});
