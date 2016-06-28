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
    
    $('#type').change(function(){
        type = $('#type').val()
        if(type == "Inventory") {
            $('#institution').parent().remove()
            $('#account_number').parent().remove()

            invenTab = $('<div class="form-group">'
                   + '<label for="">fuel type</label>'
                   + '<input type="text" id="fuel_type" class="form-control">'
                   + '</div>'
                   + '<div class="form-group">'
                   + '<label for="">location</label>'
                   + '<input type="text" id="location" class="form-control">'
                   + '</div>'
                   + '<div class="form-group">'
                   + '<label for="">id number</label>'
                   + '<input type="text" id="id_number" class="form-control">'
                   + '</div>');

            $('#type').parent().parent().append(invenTab);
        } else {
            $('#fuel_type').parent().remove()
            $('#location').parent().remove()
            $('#id_number').parent().remove()
            hedgeTab = $('<div class="form-group">'
                   + '<label for="">institution</label>'
                   + '<input type="text" id="institution" class="form-control">'
                   + '</div>'
                   + '<div class="form-group">'
                   + '<label for="">account number</label>'
                   + '<input type="text" id="account_number" class="form-control">'
                   + '</div>');
            $('#type').parent().parent().append(hedgeTab);
        }
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
        data: ({ user_name : text_vals[0], full_name: text_vals[1], email: text_vals[2], company: text_vals[3]}),
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

function remove_accounts(accounts) {
    $.ajax({
        type: "POST",
        url: "/remove_account/",
        data: ({ accounts : accounts}),
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

function add_company() {
    console.log('add company test')

    var text_vals = new Array(2);
    var i = 0;
    $("#company_info input").each(function(){
        console.log($(this).val())
        text_vals[i] = $(this).val()
        i = i + 1
    })
    
    $.ajax({
        type: "POST",
        url: "/company/create_company/",
        data: ({ company_name : text_vals[0], address: text_vals[1]}),
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

function remove_company(companies) {
    $.ajax({
        type: "POST",
        url: "/company/remove_company/",
        data: ({ companies : companies}),
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

function add_inventory() {

    var text_vals = new Array(6);
    var i = 0;
    console.log('$*********' + $('#inven_hedge_info'))
    $("#inven_hedge_info input").each(function(){
        console.log( '#########::::::' + $(this).val())
        text_vals[i] = $(this).val()
        i = i + 1
    })
    var m2m_account_id = $('#current_account_id').text()
    
    console.log('inven ***' + $('#type').val() + '$$$$')
    if($('#type').val() == 'Inventory') {
            console.log('@@@@@@@@@@@@@@@@@@@@@@@@@@')
	    $.ajax({
		type: "POST",
		url: "/inventory/create_inventory/",
		data: ({ name : text_vals[0], fuel_type: text_vals[1], in_location: text_vals[2], id_number: text_vals[3], account_id: m2m_account_id}),
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
    } else {
            console.log('!!!!!!!!!!!!!!!!!!!!')
	    $.ajax({
		type: "POST",
		url: "/hedge/create_hedge_account",
		data: ({ name : text_vals[0], institution: text_vals[1], account_number: text_vals[2]}),
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

}
