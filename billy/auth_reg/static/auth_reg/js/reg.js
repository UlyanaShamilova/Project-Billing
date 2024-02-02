$(document).ready(function(){
    $(".reg").click(function(event){
        event.preventDefault();
        var csrf_token =$("[name='csrfmiddlewaretoken']").val();
        var nameReg = $("#nameReg").val();
        var passwordReg = $("#passwordReg").val();
        var repPassword = $("#repPassword").val();

        $.ajax({
            url:"/registrations/",
            type:"POST",
            data:{username:nameReg,
                password:passwordReg,
                repPassword:repPassword,
                csrfmiddlewaretoken:csrf_token
            },

            success: function(response) {
                console.log(nameReg)
                $("#message").text("Реєстрація успішна!")
                $("#nameReg").val("")
                $("#passwordReg").val("")
                $("#repPassword").val("")
            }
        })
    })
})