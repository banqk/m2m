$(function(){
    $('#email').focus(function(){
        console.log("Please input a invalid email.");
    });
    $('#email').blur(function(){
        var myreg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
        if(!myreg.test($(this).val())){
            console.log("Please input a invalid email!");
            $(this).focus()
            
        }
    });

    $('#password1').focus(function(){
        console.log("Enter at least 6 characters.");
    });
    $('#password1').blur(function(){
        console.log("Password can not be empty");
    });
    $('#password2').focus(function(){
        console.log("Re-enter at least 6 characters.");
    });
    $('#password2').blur(function(){
        console.log("password1:" + $('#password1').val() + ",password2:" +$('#password2').val())
        if ($('#password1').val() != $(this).val()) {
            console.log("Password and re-enter password do not match.")
        }
    });
    
    $('#confirm').click(function(){
       console.log('BBBBBBBBBBBBBBBB') 
    });
});

function add_user() {

    var text_vals = new Array(6);
    var i = 0;
    $("#user_info input").each(function(){
        console.log($(this).val())
        text_vals[i] = $(this).val()
        i = i + 1
    })
    
    $.ajax({
        type: "POST",
        url: "/create_account/",
        data: ({ user_name : text_vals[0], password : text_vals[1], full_name: text_vals[3], email: text_vals[4], company: text_vals[5]}),
        success: function(html){

            json_data = JSON.parse(html);
            if (json_data.error) {
                feedback(json_data.error_message, 'error')
            } else {

                feedback('Success', 'ok');
            }
        },
        error: function(html){
            feedback('There was an error', 'error')
        }
    });

}

function add_event() {
    //$('#confirm').click
}

function remove_accounts() {
    $('#users .selected')
    console.log($('#confirm').text())
    console.log('#################')
}
