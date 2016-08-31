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
    
    $('#inventory').blur(function(){
        invent_name = $('#inventory').val()
        if(invent_name != ''){
            console.log('AAAAAAAAAAAAAAAAAbBBB')
            realtime_auto(invent_name, 'inventory')
        }
    });
    
    $('#phy_type').change(function(){
        type = $('#phy_type').val()
        if(type == "Transfer") {
            //$('#account_number').parent().remove()

            invenTab = $('<div class="form-group">'
//                   + '<label for="">to m2m account</label>'
//                   + '<input type="text" id="to_m2m_account" class="form-control">'
//                   + '</div>'
                   + '<label for="">to inventory</label>'
                   + '<input type="text" id="to_inventory" class="form-control">'
                   + '</div>');

            $('#phy_type').parent().parent().append(invenTab);
            $('#to_inventory').blur(function(){
                invent_name = $('#to_inventory').val()
                if(invent_name != ''){
                    console.log('AAAAAAAAAAAAAAAAAbCCCCC')
                    realtime_auto(invent_name, 'to_inventory')
                }
            });
            fresh_autocomplete()
        } else {
            $('#to_product').parent().parent().remove()
            $('#to_inventory').parent().parent().remove()
        }
    });

    if ($('#auto_account').text().split(",").length > 1) {
   
        var data = $('#auto_account').text()
        var input = document.getElementById('m2m_account')
        comboplete = new Awesomplete(input, {
            minChars: 0,
            //autoFirst: true,
            list: data,
        });
        Awesomplete.$('#m2m_account').addEventListener("click", function() {
	    if (comboplete.ul.childNodes.length === 0) {
		comboplete.minChars = 0;
		comboplete.evaluate();
	    }
	    else if (comboplete.ul.hasAttribute('hidden')) {
		comboplete.open();
  	    }
	    else {
		comboplete.close();
 	    }
        });
    }
    if ($('#auto_to_account').text().split(",").length > 1) {
        var data1 = $('#auto_to_account').text()
        var input1 = document.getElementById('to_m2m_account')
        comboplete1 = new Awesomplete(input1, {
            minChars: 0,
            //autoFirst: true,
            list: data1,
        });
        Awesomplete.$('#to_m2m_account').addEventListener("click", function() {
	    if (comboplete1.ul.childNodes.length === 0) {
		comboplete1.minChars = 0;
		comboplete1.evaluate();
	    }
	    else if (comboplete1.ul.hasAttribute('hidden')) {
		comboplete1.open();
  	    }
	    else {
		comboplete1.close();
 	    }
        });
    }
    console.log('AAAAAAAAAAAAAAa  ' + $('#auto_fuel_class').text())
    if($('#auto_fuel_class').text().split(",").length > 1){
        var data =  $('#auto_fuel_class').text()
        var fuel_input = document.getElementById('fuel_class')
        fuel_comboplete = new Awesomplete(fuel_input, {
            minChars: 1,
            //autoFirst: true,
            list: data,
        });
        Awesomplete.$('#fuel_class').addEventListener("click", function() {
	    if (fuel_comboplete.ul.childNodes.length === 0) {
		fuel_comboplete.minChars = 0;
		fuel_comboplete.evaluate();
	    }
	    else if (fuel_comboplete.ul.hasAttribute('hidden')) {
		fuel_comboplete.open();
  	    }
	    else {
		fuel_comboplete.close();
 	    }
        });
    }
    if($('#auto_counter_party').text().split("$").length > 1){
        var fuel_input = document.getElementById('counter_party')
        counter_comboplete = new Awesomplete(fuel_input, {
            minChars: 1,
            //autoFirst: true,
            list: $('#auto_counter_party').text().split("$"),
        });
        Awesomplete.$('#counter_party').addEventListener("click", function() {
	    if (counter_comboplete.ul.childNodes.length === 0) {
		counter_comboplete.minChars = 0;
		counter_comboplete.evaluate();
	    }
	    else if (counter_comboplete.ul.hasAttribute('hidden')) {
		counter_comboplete.open();
  	    }
	    else {
		counter_comboplete.close();
 	    }
        });
    }
    if($('#auto_product').text().split(",").length > 1){
        var fuel_input = document.getElementById('product')
        prod_comboplete = new Awesomplete(fuel_input, {
            minChars: 1,
            //autoFirst: true,
            list: $('#auto_product').text().split(",")
        });
        Awesomplete.$('#product').addEventListener("click", function() {
	    if (prod_comboplete.ul.childNodes.length === 0) {
		prod_comboplete.minChars = 0;
		prod_comboplete.evaluate();
	    }
	    else if (prod_comboplete.ul.hasAttribute('hidden')) {
		prod_comboplete.open();
  	    }
	    else {
		prod_comboplete.close();
 	    }
        });
    }
    if($('#auto_inventory').text().split(",").length > 1){
        var invent_input = document.getElementById('inventory')
        invent_comboplete = new Awesomplete(invent_input, {
            minChars: 1,
            //autoFirst: true,
            list: $('#auto_inventory').text()
        });
        Awesomplete.$('#inventory').addEventListener("click", function() {
	    if (invent_comboplete.ul.childNodes.length === 0) {
		invent_comboplete.minChars = 0;
		invent_comboplete.evaluate();
	    }
	    else if (invent_comboplete.ul.hasAttribute('hidden')) {
		invent_comboplete.open();
  	    }
	    else {
		invent_comboplete.close();
 	    }
        });
    }
    if($('#auto_to_inventory').text().split(",").length > 1){
        var invent_input1 = document.getElementById('to_inventory')
        invent_comboplete1 = new Awesomplete(invent_input1, {
            minChars: 1,
            //autoFirst: true,
            list: $('#auto_to_inventory').text().split(",")
        });
        Awesomplete.$('#to_inventory').addEventListener("click", function() {
	    if (invent_comboplete1.ul.childNodes.length === 0) {
		invent_comboplete1.minChars = 0;
		invent_comboplete1.evaluate();
	    }
	    else if (invent_comboplete1.ul.hasAttribute('hidden')) {
		invent_comboplete1.open();
  	    }
	    else {
		invent_comboplete1.close();
 	    }
        });
    }
    if($('#auto_hedge_account').text().split(",").length > 1){
        var fuel_input = document.getElementById('hedge_account')
        hedge_comboplete = new Awesomplete(fuel_input, {
            minChars: 1,
            //autoFirst: true,
            list: $('#auto_hedge_account').text().split(",")
        });
        Awesomplete.$('#hedge_account').addEventListener("click", function() {
	    if (hedge_comboplete.ul.childNodes.length === 0) {
		hedge_comboplete.minChars = 0;
		hedge_comboplete.evaluate();
	    }
	    else if (hedge_comboplete.ul.hasAttribute('hidden')) {
		hedge_comboplete.open();
  	    }
	    else {
		hedge_comboplete.close();
 	    }
        });
    }
    if($('#auto_instrument').text().split(",").length > 1){
        var fuel_input = document.getElementById('instrument')
        inst_comboplete = new Awesomplete(fuel_input, {
            minChars: 1,
            //autoFirst: true,
            list: $('#auto_instrument').text().split(",")
        });
        Awesomplete.$('#instrument').addEventListener("click", function() {
	    if (inst_comboplete.ul.childNodes.length === 0) {
		inst_comboplete.minChars = 0;
		inst_comboplete.evaluate();
	    }
	    else if (inst_comboplete.ul.hasAttribute('hidden')) {
		inst_comboplete.open();
  	    }
	    else {
		inst_comboplete.close();
 	    }
        });
    }

    $('.form_datetime').datetimepicker({format: 'YYYY-MM-DD HH:mm'});

});

function realtime_auto(name, type) {
    var product_list = ''
    $.ajax({
        type: "POST",
        url: "/api/get_prod/",
        data: ({ name : name}),
        success: function(html){

            json_data = JSON.parse(html);
            if (json_data.error) {
                bootbox.alert(json_data['response'])
            } else {
                //bootbox.alert(json_data['response'])
                if(json_data['response'] == 'success'){
                    product_list = json_data['products'] 
                    console.log(product_list)
                    if(product_list == '') {
                        bootbox.alert("The inventory don't include anyone product.")
                    } 
                    if(product_list.split(",").length > 1){
                        console.log('WWWWWWWWWWWWWWWWWWWWWWW44444')
                        if(type == 'inventory'){
                            invenTab = $('<input type="text" id="product" class="form-control">');
                            var s_parent = $('#product').parent().parent()
                            $('#product').parent().remove()
                            s_parent.append(invenTab)
                            var invent_input = document.getElementById('product')
                            prod_comboplete = new Awesomplete(invent_input, {
                                minChars: 1,
                                list: product_list,
                            });
                            Awesomplete.$('#product').addEventListener("click", function() {
	                        if (prod_comboplete.ul.childNodes.length === 0) {
		                    prod_comboplete.minChars = 0;
		                    prod_comboplete.evaluate();
                                    console.log('WWWWWWWWWWWWWWWWWWWWWWW44444')
	                        }
	                        else if (prod_comboplete.ul.hasAttribute('hidden')) {
		                    prod_comboplete.open();
  	                        }
	                        else {
		                    prod_comboplete.close();
 	                        }
                            });
                        
                        } else {
                            invenTab = $('<input type="text" id="to_product" class="form-control">');
                            var s_parent = $('#to_product').parent().parent()
                            $('#to_product').parent().remove()
                            s_parent.append(invenTab)
                            var invent_input = document.getElementById('to_product')
                            to_prod_comboplete = new Awesomplete(invent_input, {
                                minChars: 1,
                                list: product_list,
                            });
                            Awesomplete.$('#to_product').addEventListener("click", function() {
	                        if (to_prod_comboplete.ul.childNodes.length === 0) {
		                    to_prod_comboplete.minChars = 0;
		                    to_prod_comboplete.evaluate();
                                    console.log('WWWWWWWWWWWWWWWWWWWWWWW44444')
	                        }
	                        else if (to_prod_comboplete.ul.hasAttribute('hidden')) {
		                    to_prod_comboplete.open();
  	                        }
	                        else {
		                    to_prod_comboplete.close();
 	                        }
                            });
                            
                        }
                    }
                }
            }
        },
        error: function(html){
            bootbox.alert("There was an error.")
        }
    });
}

function fresh_autocomplete(){
    if ($('#auto_to_account').text().split(",").length > 1) {
        var data1 = $('#auto_to_account').text()
        var input1 = document.getElementById('to_m2m_account')
        comboplete1 = new Awesomplete(input1, {
            minChars: 0,
            //autoFirst: true,
            list: data1,
        });
        Awesomplete.$('#to_m2m_account').addEventListener("click", function() {
	    if (comboplete1.ul.childNodes.length === 0) {
		comboplete1.minChars = 0;
		comboplete1.evaluate();
	    }
	    else if (comboplete1.ul.hasAttribute('hidden')) {
		comboplete1.open();
  	    }
	    else {
		comboplete1.close();
 	    }
        });
    }
    if($('#auto_to_inventory').text().split(",").length > 1){
        var fuel_input1 = document.getElementById('to_inventory')
        invent_comboplete1 = new Awesomplete(fuel_input1, {
            minChars: 1,
            //autoFirst: true,
            list: $('#auto_to_inventory').text().split(",")
        });
        Awesomplete.$('#to_inventory').addEventListener("click", function() {
	    if (invent_comboplete1.ul.childNodes.length === 0) {
		invent_comboplete1.minChars = 0;
		invent_comboplete1.evaluate();
	    }
	    else if (invent_comboplete1.ul.hasAttribute('hidden')) {
		invent_comboplete1.open();
  	    }
	    else {
		invent_comboplete1.close();
 	    }
        });
    }

}

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
        data: ({ name : text_vals[0], fuel_class: text_vals[2], description: text_vals[1], account: text_vals[3], inventory: text_vals[4]}),
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
    phy_type = $('#phy_type').val()
    if (phy_type == 'Transfer') {
        $.ajax({
            type: "POST",
            url: "/transaction/create_phy/",
            data: ({ name : text_vals[0], type: $("#physical_info select").val(), inventory: text_vals[1], product: text_vals[2], net_volume: text_vals[3],to_inventory: text_vals[4], gross_volume: text_vals[5], price: text_vals[6], program: text_vals[7], counter: text_vals[8]}),
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
            data: ({ name : text_vals[0], type: $("#physical_info select").val(), inventory: text_vals[1], product: text_vals[2], net_volume: text_vals[3], gross_volume: text_vals[4], price: text_vals[5], program: text_vals[6], counter: text_vals[7]}),
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
    
    $.ajax({
        type: "POST",
        url: "/hedge_tran/create_ht/",
        data: ({ name : text_vals[0], type: $("#phy_type").val(), hedge_account: text_vals[1], inventory: text_vals[2], contract: text_vals[3], volume: text_vals[4], price: text_vals[5],initial_pos: $('#initial_pos').val(), confirm_number:text_vals[6], trader: text_vals[7],ht_status: $("#status").val(), program:text_vals[8]}),
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
