$(function(){

    $('#name').focus(function(){
        console.log("The name is not empty and greater than 5 characters.")
    });

    $('#name').blur(function(){
        name = $('#name').val()
        console.log(name + ',' + name.length) 
        if(name.length <= 5) {
            if($('p').length == 0) {
                pTab = $('<p style="color:red; dispaly:inline-block;">Please enter greater than 5 characters.</p>')
                $(this).after(pTab)
            }
            $(this).focus()
        } else {
            $('p').remove();
        }
    });
   
    $('#address').focus(function(){
        console.log("enter address input tab")
    }); 
    $('#address').blur(function(){
        address = $('#address').val();
        if(address.length < 1){
            console.log('################')
            if($('p').length == 0) {
                pTab = $('<p style="color:red; dispaly:inline-block;">The address cannot be empty.</p>');
                $(this).after(pTab);
            }
            $(this).focus();
        } else {
            $('p').remove();
        }
    });

    $('#fuel_type').blur(function(){
        fuel_type = $('#fuel_type').val();
        if(fuel_type.length < 1){
            if($('p').length == 0) {
                pTab = $('<p style="color:red; dispaly:inline-block;">The fuel type cannot be empty.</p>');
                $(this).after(pTab);
            }
            $(this).focus();
        } else {
            $('p').remove();
        }
    });
    $('#id_number').blur(function(){
        id_number = $('#id_number').val();
        if(id_number.length < 1){
            if($('p').length == 0) {
                pTab = $('<p style="color:red; dispaly:inline-block;">The id number cannot be empty.</p>');
                $(this).after(pTab);
            }
            $(this).focus();
        } else {
            $('p').remove();
        }
    });

    $('#institution').blur(function(){
        institution = $('#institution').val();
        if(institution.length < 1){
            if($('p').length == 0) {
                pTab = $('<p style="color:red; dispaly:inline-block;">The institution cannot be empty.</p>');
                $(this).after(pTab);
            }
            $(this).focus();
        } else {
            $('p').remove();
        }
    });
    $('#account_number').blur(function(){
        account_number = $('#account_number').val();
        if(account_number.length < 1){
            if($('p').length == 0) {
                pTab = $('<p style="color:red; dispaly:inline-block;">The account number cannot be empty.</p>');
                $(this).after(pTab);
            }
            $(this).focus();
        } else {
            $('p').remove();
        }
    });
/*
    $('#address').blur(function(){
        address = $('#address').val();
        if(name.length < 1){
            pTab = $('<p style="color:red; dispaly:inline-block;">The address cannot be empty.</p>');
            $(this).after(pTab)
            $(this).focus()
        } else {
            $('p').remove();
        }
    });
*/
    $('#email').focus(function(){
        console.log("Please input a invalid email.");
    });
    $('#email').blur(function(){
        var myreg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
        if(!myreg.test($(this).val())){
            console.log("Please input a invalid email!");
            if($('p').length<1) {
                pTab = $('<p style="color:red; dispaly:inline-block;">Please enter a invalid email.</p>');
                $(this).after(pTab);
            }
            $(this).focus();
            
        } else {
            $('p').remove();
        }
    });

    $('#password').blur(function(){
        password = $('#password').val()
        console.log(name + ',' + name.length) 
        if(password.length <= 5) {
            if($('p').length == 0) {
                pTab = $('<p style="color:red; dispaly:inline-block;">Please enter greater than 5 characters.</p>')
                $(this).after(pTab)
            }
            $(this).focus()
        } else {
            $('p').remove();
        }
    });

    $('#confirm').blur(function(){
        console.log("password:" + $('#password1').val() + ",password2:" +$('#password2').val())
        if ($('#password').val() != $(this).val()) {
            if($('p').length == 0) {
                pTab = $('<p style="color:red; dispaly:inline-block;">Password ad re-enter password do not match.</p>')
                $(this).after(pTab)
            }
            $(this).focus()
        } else {
            $('p').remove();
        }
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

    if ($('#auto_account').text().split(",").length > 1) {
   
        var input = document.getElementById('m2m_account')
        new Awesomplete(input, {
            list: $('#auto_account').text().split(",")
        });
    }
    if($('#auto_fuel_class').text().split(",").length > 1){
        var fuel_input = document.getElementById('fuel_class')
        new Awesomplete(fuel_input, {
            list: $('#auto_fuel_class').text().split(",")
        });
    }

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
        data: ({ name : text_vals[0], address: text_vals[1], email: text_vals[2]}),
        success: function(html){

            json_data = JSON.parse(html);
            if (json_data.error) {
                bootbox.alert(json_data['response'])
            } else {
                //bootbox.alert(json_data['response'])
                if(json_data['response'] == 'success'){
                    window.location = "/accounts";
                } else {
                    bootbox.alert(json_data['info']);
                }
            }
        },
        error: function(html){
            bootbox.alert("There was an error.")
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
            bootbox.alert("There was an error.")
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
            bootbox.alert("There was an error.")
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
            bootbox.alert("There was an error.")
        }
    });
}

function add_inventory(entityType) {

    var text_vals = new Array(6);
    var m2m_account_id = $('#current_account_id').text()
    
    console.log('inven ***' + $('#type').val() + '$$$$')
    if(entityType == 'Inventory') {
        var i = 0;
        console.log('$*********' + $('#inven_hedge_info'))
        $("#inven_hedge_info input").each(function(){
            console.log( '#########::::::' + $(this).val())
            text_vals[i] = $(this).val()
            i = i + 1
        })
	    $.ajax({
		type: "POST",
		url: "/inventory/create_inventory/",
		data: ({ name : text_vals[0], fuel_type: $("#inven_hedge_info select").val(), in_location: text_vals[1], id_number: text_vals[2], account_id: m2m_account_id}),
		success: function(html){
		    json_data = JSON.parse(html);
                    console.log(json_data['account_id'])
                    window.location.href='/api/account/?account_id=' + json_data['account_id']
		    if (json_data.error) {
			feedback(json_data.error_message, 'error')
		    } else {

			feedback('Success', 'ok');
		    }
		},
		error: function(html){
                    bootbox.alert("There was an error.")
		}
	    });
    } else {
        var i = 0;
        console.log('$*********' + $('#inven_hedge_info2'))
        $("#inven_hedge_info2 input").each(function(){
            console.log( '#########::::::' + $(this).val())
            text_vals[i] = $(this).val()
            i = i + 1
        })
	    $.ajax({
		type: "POST",
		url: "/hedge/create_hedge_account/",
		data: ({ name : text_vals[0], institution: text_vals[1], account_number: text_vals[2], account_id: m2m_account_id}),
		success: function(html){

		    json_data = JSON.parse(html);
                    window.location.href='/api/account/?account_id=' + json_data['account_id']
		    if (json_data.error) {
			feedback(json_data.error_message, 'error')
		    } else {

			feedback('Success', 'ok');
		    }
		},
		error: function(html){
                    bootbox.alert("There was an error.")
		}
	    });

    }

}


function new_inventory() {
    var text_vals = new Array(6);
    var i = 0;
    $("#inventory_info input").each(function(){
        console.log( '#########::::::' + $(this).val())
        text_vals[i] = $(this).val()
        i = i + 1
    })    
    $.ajax({
	type: "POST",
	url: "/inventory/create_inventory/",
	data: ({ name : text_vals[0], fuel_type: $("#inventory_info select").val(), in_location: text_vals[1], id_number: text_vals[2], account_id: text_vals[3]}),
	success: function(html){
	    json_data = JSON.parse(html);
//	    console.log(json_data['account_id'])
//	    window.location.href='/api/account/?account_id=' + json_data['account_id']
            if (json_data.error) {
                bootbox.alert(json_data['response'])
            } else {
                //bootbox.alert(json_data['response'])
                if(json_data['response'] == 'success'){
                    window.location = "/inventory/inventories";
                } else {
                    bootbox.alert(json_data['info']);
                }
            }
	},
	error: function(html){
            bootbox.alert("There was an error.")
	}
    });    
}

function new_hedge_account() {
    var text_vals = new Array(6);
    var i = 0;
    $("#hedge_account_info input").each(function(){
        console.log( '#########::::::' + $(this).val())
        text_vals[i] = $(this).val()
        i = i + 1
    })    
    $.ajax({
	type: "POST",
	url: "/hedge/create_hedge_account/",
	data: ({ name : text_vals[0], institution: text_vals[1], account_number: text_vals[2], account_id: text_vals[3]}),
	success: function(html){
	    json_data = JSON.parse(html);
//	    console.log(json_data['account_id'])
//	    window.location.href='/api/account/?account_id=' + json_data['account_id']
            if (json_data.error) {
                bootbox.alert(json_data['response'])
            } else {
                //bootbox.alert(json_data['response'])
                if(json_data['response'] == 'success'){
                    window.location = "/hedge_account/hedge_accounts";
                } else {
                    bootbox.alert(json_data['info']);
                }
            }
	},
	error: function(html){
            bootbox.alert("There was an error.")
	}
    });    
}

function remove_inventory(inventories) {
    $.ajax({
        type: "POST",
        url: "/inventory/remove_inventory/",
        data: ({ inventories : inventories}),
        success: function(html){

            json_data = JSON.parse(html);
            if (json_data.error) {
                feedback(json_data.error_message, 'error')
            } else {

                feedback('Success', 'ok');
            }
        },
        error: function(html){
            bootbox.alert("There was an error.")
        }
    });
}

function remove_hedge_account(hedge_accounts) {
    $.ajax({
        type: "POST",
        url: "/hedge/remove_hedge_account/",
        data: ({ hedge_accounts : hedge_accounts}),
        success: function(html){

            json_data = JSON.parse(html);
            if (json_data.error) {
                feedback(json_data.error_message, 'error')
            } else {

                feedback('Success', 'ok');
            }
        },
        error: function(html){
            bootbox.alert("There was an error.")
        }
    });
}

function update_account() {

    var text_vals = new Array(11);
    var i = 0;
    $("#edit_account input").each(function(){
        console.log( '#########::::::' + $(this).val())
        text_vals[i] = $(this).val()
        i = i + 1
    })
    var m2m_account_id = $('#current_account_id').text()
    $.ajax({
        type: "POST",
        url: "/update_account/",
        data: ({ name : text_vals[0], address: text_vals[1], email: text_vals[2], account_id: m2m_account_id}),
        success: function(html){
            json_data = JSON.parse(html);
//          console.log(json_data['account_id'])
//          window.location.href='/api/account/?account_id=' + json_data['account_id']
            if (json_data.error) {
                bootbox.alert(json_data.error_message)
            } else {
                bootbox.alert("Update success.")
            }
        },
        error: function(html){
            bootbox.alert("There was an error.")
        }
    });
}
function update_inventory() {

    var text_vals = new Array(11);
    var i = 0;
    $("#edit_inventory input").each(function(){
        console.log( '#########::::::' + $(this).val())
        text_vals[i] = $(this).val()
        i = i + 1
    })
    var inventory_id = $('#inventory_id').text()
    $.ajax({
        type: "POST",
        url: "/inventory/update_inventory/",
        data: ({ name : text_vals[0], fuel_type: text_vals[1], in_location: text_vals[2], id_number: text_vals[3],volumn: text_vals[4], inventory_id: inventory_id}),
        success: function(html){
            json_data = JSON.parse(html);
//          console.log(json_data['account_id'])
//          window.location.href='/api/account/?account_id=' + json_data['account_id']
            bootbox.alert("Update success.")
            if (json_data.error) {
                feedback(json_data.error_message, 'error')
            } else {

                feedback('Success', 'ok');
            }
        },
        error: function(html){
            bootbox.alert("There was an error.")
        }
    });
}
function update_hedge() {

    var text_vals = new Array(11);
    var i = 0;
    $("#edit_hedge input").each(function(){
        console.log( '#########::::::' + $(this).val())
        text_vals[i] = $(this).val()
        i = i + 1
    })
    var hedge_id = $('#hedge_id').text()
    $.ajax({
        type: "POST",
        url: "/hedge/update_hedge/",
        data: ({ name : text_vals[0], institution: text_vals[1], id_number: text_vals[2], hedge_id: hedge_id}),
        success: function(html){
            json_data = JSON.parse(html);
//          console.log(json_data['account_id'])
//          window.location.href='/api/account/?account_id=' + json_data['account_id']
            if (json_data.error) {
                bootbox.alert(json_data.error_message)
            } else {
                bootbox.alert("Update success.")
            }
        },
        error: function(html){
            bootbox.alert("There was an error.")
        }
    });
}
function update_user() {

    var user_id = $('#user_id').text()
    $.ajax({
        type: "POST",
        url: "/users/update/",
        data: ({ permission:$('#permission_id').val(),user_id: user_id}),
        success: function(html){
            json_data = JSON.parse(html);
            if (json_data.error) {
                bootbox.alert(json_data['response'])
            } else {
                if(json_data['response'] == 'success'){
                    bootbox.alert(json_data['info']);
                    //window.location = "/users/users";
                } else {
                    bootbox.alert(json_data['info']);
                }
            }
        },
        error: function(html){
            bootbox.alert("There was an error.")
        }
    });
}

function add_account() {

    var text_vals = new Array(9);
    var i = 0;
    $("#user_info input").each(function(){
        text_vals[i] = $(this).val()
        i = i + 1
    })
    
    $.ajax({
        type: "POST",
        url: "/users/create_user/",
        data: ({ name : text_vals[0], password: text_vals[1], first_name: text_vals[3], last_name: text_vals[4], email: text_vals[5]}),
        success: function(html){

            json_data = JSON.parse(html);
            if (json_data.error) {
                bootbox.alert(json_data['response'])
            } else {
                //bootbox.alert(json_data['response'])
                if(json_data['response'] == 'success'){
                    window.location = "/users/users";
                } else {
                    bootbox.alert(json_data['info']);
                }
            }
        },
        error: function(html){
            bootbox.alert("There was an error.")
        }
    });

}
function add_counter() {

    var text_vals = new Array(9);
    var i = 0;
    $("#counter_info input").each(function(){
        text_vals[i] = $(this).val()
        i = i + 1
    })
    
    $.ajax({
        type: "POST",
        url: "/counter/create_counter/",
        data: ({ name : text_vals[0], counter_type: text_vals[1], address: text_vals[2], identifier: text_vals[3]}),
        success: function(html){

            json_data = JSON.parse(html);
            if (json_data.error) {
                bootbox.alert(json_data['response'])
            } else {
                //bootbox.alert(json_data['response'])
                if(json_data['response'] == 'success'){
                    window.location = "/counter/counters";
                } else {
                    bootbox.alert(json_data['info']);
                }
            }
        },
        error: function(html){
            bootbox.alert("There was an error.")
        }
    });

}
function add_product() {

    var text_vals = new Array(9);
    var i = 0;
    $("#product_info input").each(function(){
        text_vals[i] = $(this).val()
        i = i + 1
    })
    
    $.ajax({
        type: "POST",
        url: "/product/create_product/",
        data: ({ name : text_vals[0], fuel_class: text_vals[1], description: text_vals[2]}),
        success: function(html){

            json_data = JSON.parse(html);
            if (json_data.error) {
                bootbox.alert(json_data['response'])
            } else {
                //bootbox.alert(json_data['response'])
                if(json_data['response'] == 'success'){
                    window.location = "/product/products";
                } else {
                    bootbox.alert(json_data['info']);
                }
            }
        },
        error: function(html){
            bootbox.alert("There was an error.")
        }
    });

}
function add_physical() {

    var text_vals = new Array(9);
    var i = 0;
    $("#physical_info input").each(function(){
        console.log('##############' + $(this).val())
        text_vals[i] = $(this).val()
        i = i + 1
    })
    
    $.ajax({
        type: "POST",
        url: "/transaction/create_phy/",
        data: ({ name : text_vals[0], type: $("#physical_info select").val(), inventory: text_vals[1], product: text_vals[2], volume: text_vals[3], price: text_vals[4],counter: text_vals[5]}),
        success: function(html){

            json_data = JSON.parse(html);
            if (json_data.error) {
                bootbox.alert(json_data['response'])
            } else {
                //bootbox.alert(json_data['response'])
                if(json_data['response'] == 'success'){
                    window.location = "/transaction/physical";
                } else {
                    bootbox.alert(json_data['info']);
                }
            }
        },
        error: function(html){
            bootbox.alert("There was an error.")
        }
    });

}
function add_hedge_tran() {

    var text_vals = new Array(9);
    var i = 0;
    $("#hedge_tran_info input").each(function(){
        console.log('##############' + $(this).val())
        text_vals[i] = $(this).val()
        i = i + 1
    })
    
    $.ajax({
        type: "POST",
        url: "/hedge_tran/create_ht/",
        data: ({ name : text_vals[0], type: $("#hedge_tran_info select").val(), hedge_account: text_vals[1], contract: text_vals[2], volume: text_vals[3], price: text_vals[4],initial_pos: text_vals[5]}),
        success: function(html){

            json_data = JSON.parse(html);
            if (json_data.error) {
                bootbox.alert(json_data['response'])
            } else {
                //bootbox.alert(json_data['response'])
                if(json_data['response'] == 'success'){
                    window.location = "/hedge_tran/hedge_tran";
                } else {
                    bootbox.alert(json_data['info']);
                }
            }
        },
        error: function(html){
            bootbox.alert("There was an error.")
        }
    });

}

function add_fuel_class() {

    var text_vals = new Array(9);
    var i = 0;
    $("#fuel_class_info input").each(function(){
        console.log('##############' + $(this).val())
        text_vals[i] = $(this).val()
        i = i + 1
    })
    
    $.ajax({
        type: "POST",
        url: "/fuel/create_fuel/",
        data: ({ code : text_vals[0], description: text_vals[1], account_id: text_vals[2]}),
        success: function(html){

            json_data = JSON.parse(html);
            if (json_data.error) {
                bootbox.alert(json_data['response'])
            } else {
                //bootbox.alert(json_data['response'])
                if(json_data['response'] == 'success'){
                    window.location = "/fuel/fuels";
                } else {
                    bootbox.alert(json_data['info']);
                }
            }
        },
        error: function(html){
            bootbox.alert("There was an error.")
        }
    });

}

function add_instrument() {

    var text_vals = new Array(9);
    var i = 0;
    $("#instrument_info input").each(function(){
        console.log('##############' + $(this).val())
        text_vals[i] = $(this).val()
        i = i + 1
    })
    
    $.ajax({
        type: "POST",
        url: "/inst/create_inst/",
        data: ({ symbol : text_vals[0], fuel_class: text_vals[1], year: text_vals[2], month: text_vals[3], expiration_date: text_vals[4], instrument: text_vals[5],put_call: text_vals[6], strike_price: text_vals[7], counter_party: text_vals[8]}),
        success: function(html){

            json_data = JSON.parse(html);
            if (json_data.error) {
                bootbox.alert(json_data['response'])
            } else {
                //bootbox.alert(json_data['response'])
                if(json_data['response'] == 'success'){
                    window.location = "/inst/hedge_inst";
                } else {
                    bootbox.alert(json_data['info']);
                }
            }
        },
        error: function(html){
            bootbox.alert("There was an error.")
        }
    });

}
