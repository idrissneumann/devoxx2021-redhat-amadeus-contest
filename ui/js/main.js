function loadFlights(api_url){
    var dataObj = {};
    
    dataObj["departure_date"] = $("#departure_date").val();
    dataObj["origin"] = $("#origin").val();
    dataObj["destination"] = $("#destination").val();

    var colOptions = [
      {"sTitle": "Depature", sWidth: '20%', "sType":"string", "bSortable": true},
      {"sTitle": "Arrival", sWidth: '20%', "sType":"string", "bSortable": true},
      {"sTitle": "Price", sWidth: '20%', "sType":"string", "bSortable": true},
      {"sTitle": "Timestamp", sWidth: '20%', "sType":"string", "bSortable": true}
    ];
               
    templateDatatable = $("#contentTable");
    templateDatatable.html('<div style="text-align: center;">Loading ...</div>');
    
    vhtml = '<thead><tr>';
    var i, nbColonnes = 4;
    for (i = 0 ; i < nbColonnes ; i++){
        vhtml += '<th></th>';
    }
    vhtml += '</tr></thead><tbody></tbody>';
    
    $.ajax({  
        type : "Get",   
        url : api_url + '/v1/amadeus?as_array=true',
        data : dataObj,
        success : function(response) {
            templateDatatable.html('<table name="datatable" class="datatable"><tr></tr></table>');
            // Injection of content
            templateDatatable.find('table[name="datatable"]').html(vhtml);            
            datatable = templateDatatable.find('table[name="datatable"]').dataTable({
                 "bPaginate"        : true,
                 "iDisplayLength"    : dataObj["maxPage"]
                 ,"bProcessing"        : true
                 ,"aaData"            : response
                 ,"sPaginationType" : "full_numbers"
                 ,"bDestroy"        : true
                 ,"bFilter"            : false
                 ,"bAutoWidth"        : false
                 ,"bLengthChange"    : true
                 ,"bSort"            : true
                 ,"aoColumns"        : colOptions
                 ,"oLanguage"        :{
                    "sZeroRecords"    : "Not found",
                    "sInfoEmpty"    : "",
                    "sInfo"         : "",
                    "sLengthMenu"     : "",
                    "sProcessing"    : "Loading",
                    "sInfoFiltered"    : ""
                }
            });
        },  
        error : function(e) {  
            $("#contentTable").html(e);
        }  
    }); 
}