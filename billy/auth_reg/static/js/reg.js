$(document).ready(function(){
    const nameReg = $("#nameReg").val();
    const passwordReg = $("#passwordReg").val();
    const repPassword = $("#repPassword").val();
    
    if (passwordReg != repPassword){
        alert("IDI V LES")
        console.log("IDI V 3 REIX")
        return
}
    $.ajax({
        url:"reg",
        type:"POST",
        data:{nameReg:nameReg,
            passwordReg:passwordReg,
            repPassword:repPassword,
        },

        success: function(response) {
            console.log(response)
        }
    })
})