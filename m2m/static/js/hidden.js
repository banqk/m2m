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
    
    $('#inventory').change(function(){
        var invent_name = $('#inventory').val()
        if(invent_name != ''){
             data = JSON.parse($("#all_inventory_product").text());
             for(var i=0;i<data.length;i++) {
                if ((data[i].inv) == (invent_name)) {
                     $("#product").empty();
                     if (data[i].products.length == 0) {
                        bootbox.alert("There is no product in the inventory");
                     } else {
                        $.each(data[i].products, function(idx, p) {
                          $("#product").append($("<option></option>").attr("value", p.id).text(p.name));
                        });
                     }
                }
             }
        }
    });

    $('#hedge_account').change(function(){
        var hedge_account = $('#hedge_account').val()
        if(hedge_account != ''){
             data = JSON.parse($("#all_hedge_inventory").text());
             for(var i=0;i<data.length;i++) {
                if ((data[i].account) == (hedge_account)) {
                     $("#inventory").empty();
                     if (data[i].invs.length == 0) {
                        bootbox.alert("There is no inventory in the m2m account");
                     } else {
                        $.each(data[i].invs, function(idx, p) {
                          $("#inventory").append($("<option></option>").attr("value", p.name).text(p.name));
                        });
                     }
                }
             }
        }
    });

    $('#phy_type').change(function(){
        type = $('#phy_type').val()
        if(type == "Transfer") {
            //$('#account_number').parent().remove()
            var options = "";
            data = JSON.parse($("#all_inventory_product").text());
            for(var i=0;i<data.length;i++) {
                options += '<option value="'+data[i].inv+'">'+data[i].inv+'</option>';
            }
            invenTab = $('<div class="form-group">'
                   + '<label for="">to inventory</label>'
                   + '<select id="to_inventory" class="form-control">'
                   + options
                   + '</select>'
                   + '</div>');

            $('#phy_type').parent().parent().append(invenTab);
        } else {
            $('#to_inventory').parent().remove();
        }
        $("#counter_party").empty();
        var counters = [];
        if (type == "Sell") {
            counters = $('#auto_customer_counter').text().split("$")
        } else if (type == "Purchase") {
            counters = $('#auto_supplier_counter').text().split("$")
        } else {
            counters = $('#auto_customer_counter').text().split("$")
            counters.push.apply(counters, $('#auto_supplier_counter').text().split("$"))
        }
        $.each(counters, function(idx, p) {
            $("#counter_party").append($("<option></option>").attr("value", p).text(p));
        });
    });

    $('.form_datetime').datetimepicker({format: 'YYYY-MM-DD HH:mm'});
    $('#trans_date').datetimepicker({
        defaultDate: new Date(),
        format: 'YYYY-MM-DD HH:mm'
    });
    $('#year_date').datetimepicker({
        defaultDate: new Date(),
        format: 'YYYY'
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
        if (!$("#inven_hedge_info select").val()) {
            bootbox.alert("Please add fuel type in account page firstly.");
            return;
        }
	    $.ajax({
		type: "POST",
		url: "/inventory/create_inventory/",
		data: ({ name : text_vals[0], fuel_type: $("#inven_hedge_info select").val(), in_location: text_vals[1], id_number: text_vals[2], volume: text_vals[3], account_id: m2m_account_id}),
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
	data: ({ name : text_vals[0], fuel_type: $("#inventory_info select").val(), in_location: text_vals[1], id_number: text_vals[2],volume:text_vals[3], account_id: text_vals[4]}),
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


function add_fuel_type() {
    var m2m_account_id = $('#current_account_id').text()
    var fuel_type = $("#fuel_type").val()
    if (!fuel_type) {
        bootbox.alert("please input fuel type.")
        return;
    }
    $.ajax({
        type: "POST",
        url: "/update_account/",
        data: ({ fuel_type : fuel_type, account_id: m2m_account_id}),
        success: function(html){
            json_data = JSON.parse(html);
            if (json_data.error) {
                bootbox.alert(json_data.error_message)
            } else {
                location.reload();
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
function update_product() {
    var text_vals = new Array(11);
    var i = 0;
    $("#edit_product input").each(function(){
        console.log( '#########::::::' + $(this).val())
        text_vals[i] = $(this).val()
        i = i + 1
    })
    var product_id = $('#product_id').text()
    $.ajax({
        type: "POST",
        url: "/product/update_product/",
        data: ({ name : text_vals[0], description: text_vals[1], fuel_class: text_vals[2], product_id: product_id}),
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
function update_counter() {
    var text_vals = new Array(11);
    var i = 0;
    $("#edit_counter input").each(function(){
        console.log( '#########::::::' + $(this).val())
        text_vals[i] = $(this).val()
        i = i + 1
    })
    var counter_id = $('#counter_id').text()
    $.ajax({
        type: "POST",
        url: "/counter/update_counter/",
        data: ({ name : text_vals[0], counter_type: text_vals[1], address: text_vals[2], counter_id: counter_id}),
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
function update_fuel() {
    var text_vals = new Array(11);
    var i = 0;
    $("#edit_fuel input").each(function(){
        console.log( '#########::::::' + $(this).val())
        text_vals[i] = $(this).val()
        i = i + 1
    })
    var fuel_id = $('#fuel_id').text()
    $.ajax({
        type: "POST",
        url: "/fuel/update_fuel/",
        data: ({ code : text_vals[0], description: text_vals[1], fuel_id: fuel_id}),
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
        data: ({ name : text_vals[0], counter_type: $("#counter_info select").val(), address: text_vals[1], identifier: text_vals[2]}),
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
        data: ({ name : text_vals[0], description: text_vals[1], fuel_class: $("#fuel_class").val(), account: $("#m2m_account").val()}),
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

    var text_vals = new Array(15);
    var i = 0;
    $("#physical_info input").each(function(){
        console.log('##############' + $(this).val())
        text_vals[i] = $(this).val()
        i = i + 1
    })
    if ($("#inventory").val() == "None") {
        bootbox.alert("Please select an inventory.")
        return;
    }
    phy_type = $('#phy_type').val()
    if (phy_type == 'Transfer') {
        $.ajax({
            type: "POST",
            url: "/transaction/create_phy/",
            data: ({ name : text_vals[0], type: $("#physical_info select").val(), inventory: $("#inventory").val(),
                product: $("#product").val(), net_volume: text_vals[1],to_inventory: $("#to_inventory").val(),
                to_product: $("#product").val(), gross_volume: text_vals[2], price: text_vals[3],
                program: text_vals[4], counter: $("#counter_party").val(), trans_date: text_vals[5]}),
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

    } else {
        $.ajax({
            type: "POST",
            url: "/transaction/create_phy/",
            data: ({ name : text_vals[0], type: $("#physical_info select").val(),
            inventory: $("#inventory").val(), product: $("#product").val(), net_volume: text_vals[1],
            gross_volume: text_vals[2], price: text_vals[3], program: text_vals[4],
            counter: $("#counter_party").val(), trans_date: text_vals[5]}),
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

}
function add_hedge_tran() {

    var text_vals = new Array(9);
    var i = 0;
    $("#hedge_tran_info input").each(function(){
        console.log('##############' + $(this).val())
        text_vals[i] = $(this).val()
        i = i + 1
    })
    if ($("#hedge_account").val() == "None") {
        bootbox.alert("Please select a hedge account.")
        return;
    }
    if ($("#product").val() == null) {
        bootbox.alert("No product is selected")
        return;
    }
    $.ajax({
        type: "POST",
        url: "/hedge_tran/create_ht/",
        data: ({ name : text_vals[0], type: $("#hedge_trans_type").val(), hedge_account: $("#hedge_account").val(),
        inventory: $("#inventory").val(),product: $("#product").val(), contract: $("#instrument").val(), volume: text_vals[1],
        price: text_vals[2],initial_pos: $('#initial_pos').val(), confirm_number:text_vals[3],
        trader: text_vals[4],ht_status: $("#status").val(), program:text_vals[5]}),
        success: function(html){

            json_data = JSON.parse(html);
            if (json_data.error) {
                bootbox.alert(json_data['response'])
            } else {
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
        data: ({ code : text_vals[0], description: text_vals[1], account_name: $("#m2m_account").val()}),
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
        data: ({ instrument : text_vals[0], fuel_class: $("#fuel_class").val(), year: text_vals[1],
        month: $("#contract_month").val(), expiration_date: text_vals[2],put_call: text_vals[3],
        strike_price: text_vals[4], counter_party: $("#counter_party").val()}),
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

function add_to_inventory() {
    //var text_vals = new Array(50);
    var text_vals = new Array();
    var i = 0;
    console.log($("#add_to_inventory input"))
    var check_flag = false;
    var id = 0
    var volume = 0
    $("#add_to_inventory input").each(function(){
        console.log('AAAAAAA' + this.checked)
        //var row_value = {'id':'', 'volume': '', 'price': '0.0'}
        if( $(this).attr('type') == 'checkbox' && this.checked){
            console.log('********' + $(this).val())
            //text_vals[i] = $(this).val()
            //i = i + 1
            id = $(this).val()
            check_flag = true
        } else if($(this).attr('type') == 'checkbox'){
            check_flag = false
        }
        if(check_flag && $(this).attr('type') == 'text') {
            if($(this).attr('id') == 'p_price') {
                var row_value = new Object()
                row_value.id = id
                row_value.volume = volume
                row_value.price = $(this).val()
                text_vals.push(row_value)
                i = i + 1
            } else{
                volume = $(this).val()
            
            }
        }
    })
    post_data = JSON.stringify(text_vals)
    $.ajax({
        type: "POST",
        url: "/inventory/add_product/",
        data: ({ invent_id: $('#inventory_id').text(), products: post_data}),
        success: function(html){

            json_data = JSON.parse(html);
            if (json_data.error) {
                bootbox.alert(json_data['response'])
            } else {
                //bootbox.alert(json_data['response'])
                if(json_data['response'] == 'success'){
                    window.location = "/api/inventory/?inventory_id=" + $('#inventory_id').text();
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
