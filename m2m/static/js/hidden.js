$(function(){
    
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
                // remove the project slice from the DOM
                $('#project_slice_'+project_id).remove();

                // audit the value
                audit_values();
                feedback('Success', 'ok');
                closeWait();
            }
        },
        error: function(html){
            alert('failure');
        }
    });

}
