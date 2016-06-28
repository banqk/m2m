$(document).ready(function() {
    
    var App = {
        init: function() {
            $('.table.is-datatable').DataTable({
                columnDefs: [
                    {
                        orderable: false,
                        className: 'select-checkbox',
                        targets: 0
                    }
                ],
                dom: 'rtip',
                buttons: [
                    {
                        extend: 'print',
                        text: 'print',
                        exportOptions: {
                            modifier: {
                                selected: true
                            }
                        }
                    }
                ],
                select: {
                    style: 'multi',
                    selector: 'td:first-child'
                },
                order: [[1, 'asc']],
                initComplete: function () {
                    this.api().columns().every( function () {
                        var column = this;
                        var hasFilter = !$(column.header()).hasClass('no-filter');
                        if(hasFilter) {
                            var select = $('<select class="form-control"><option value=""></option></select>')
                                .appendTo( $(column.footer()).empty() )
                                .on('change', function () {
                                    var val = $.fn.dataTable.util.escapeRegex(
                                        $(this).val()
                                    );
             
                                    column.search( val ? '^'+val+'$' : '', true, false )
                                          .draw();
                                } );
             
                            column.data().unique().sort().each( function ( d, j ) {
                                select.append( '<option value="'+d+'">'+d+'</option>' )
                            } );                            
                        }

                    } );
                }
            });

            this.eventsHandler();
        },
        eventsHandler: function() {
            $('.select-all').on('change', function() {
                var table = $(this).parents('table').DataTable();
                TableUtils.selectAll(table, $(this));
            });

            /** 
             * Custom search for datatable
             * input[type=search] should be a parent of .table-container
             */
            $('.table-search input[type=search]').on('keyup', function() {
                var table = TableUtils.getDataTableFromControl($(this));
                table.search($(this).val()).draw();
            });

            $('.table-container .btn-print').on('click', function() {
                var table = TableUtils.getDataTableFromControl($(this));
                table.button(0).trigger();
            })

            $('.table-container .btn-delete').on('click', function() {
                var option = $(this).attr('id')
                var table = TableUtils.getDataTableFromControl($(this));
                var count = table.rows( { selected: true } ).count();
                //var choies = table.rows('.selected')
                var choices = $('.selected td');
                var len = choices.length;
                var del_list = new Array();
                if(count === 0) {
                    bootbox.alert("Please select, at least, 1 row to be deleted");
                } else {
                    bootbox.confirm("Are you sure you want to delete " + count + " item(s) ?", function(result) {
                        if(result === true) {
                            table.rows('.selected').remove().draw(false);
                        }
                    });                    
                }
                if(option == "delete_account") { 
                    for(var i=1; i<len; i+=6) {
                        del_list.push(choices.eq(i).text());
                    }
                    $('#confirm').on('click', function(){
                        remove_accounts(del_list);
                    });
                } else if(option == "delete_company") {
                    for(var i=1; i<len; i+=5) {
                        console.log('############' + choices.eq(i).text())
                        del_list.push(choices.eq(i).text());
                    }
                    console.log(del_list)
                    $('#confirm').on('click', function(){
                        remove_company(del_list);
                    });
                    
                }

            });

            //$('.date-picker').datetimepicker({
            //    format: 'MM/DD/YYYY'
            //});
        }
    }

    var TableUtils = {
        selectAll: function(table, checkbox) {
            var rows = table.cells().nodes();
            console.log(rows);
            $(rows).find(':checkbox').prop('checked', true);
        },
        getDataTableFromControl: function(elt) {
            return $(elt).parents('.table-container').find('table').DataTable();
        }
    }
    App.init();
});

