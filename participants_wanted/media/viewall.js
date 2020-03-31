
//Filter experiments
function filt() {
        var filter = document.getElementById('filter').value;
        console.log(filter);
        $.get('/experimenter/getall/', {filter: filter}, function (data) {
            if(filter === 'low') {
                data.sort((a, b) => parseFloat(a.fields['price']) - parseFloat(b.fields['price']));
                $( "#val" ).empty();
            }
            if(filter === 'high') {
                data.sort((a, b) => parseInt(b.fields['price']) - parseInt(a.fields['price']));
                $( "#val" ).empty();
            }
            if(filter == 'soon') {
                data.sort((a, b) => new Date(a.fields['start_date']) - new Date(b.fields['start_date']));
                $( "#val" ).empty();
            }
            if(filter == 'late') {
                data.sort((a, b) => new Date(b.fields['start_date']) - new Date(a.fields['start_date']));
                $( "#val" ).empty();
            }
            load(data);
        });
    }


    var apply = [];

    //View exper that can be bid on
    function appl(){
        $( "#val" ).empty();
        console.log(apply)
        if(apply.length === 0){
            $('#val').append('<h6>You are not eligible for any experiments</h6>')

        }else{
            load(apply)
        }
    }

	$(document).ready(function() {
	    //Load expr's from back end when browser loads
        $.get('/experimenter/getall/', function (data) {
            console.log(data);
            load(data)
        });

        //Bid on expr
        $(document).on('click', '.btn-success', function() {
            var name = $(this).attr('value');
            $(this).remove();
            $.get('/student/makebid/',
                {'expr_name': name, 'username':username, 'u_id':u_id}, function(){
                }

             )
        })
     });


	function load(exprs) {
	    //Dynamiclly load all expr with all information into collapsable card and append to body
        apply = [];
        console.log(x)
        var counter = 0;
         	for(i in exprs) {
                if (exprs[i].fields.expr_done === false && exprs[i].fields.expr_full === false ) {
                    $('#val').append(
                        '<div class="col-md-6">' +
                        '<div class="card shadow-sm">' +
                        '<div class="card-header">' +
                        '<h4 class="my-0 font-weight-normal">' + exprs[i].fields.name + '</h4> ' +
                        '</div>' +
                        '<div id = "' + i + '" class="card-body"> ' +
                        '<ul class="list-unstyled mt-3 mb-4"> ' +
                        '<li>Start Date: ' + new Date(exprs[i].fields.start_date).getDate()+ '-' + new Date(exprs[i].fields.start_date).getMonth() + '-' +new Date(exprs[i].fields.start_date).getFullYear() + '</li>' +
                        '<li>End Date: '  + new Date(exprs[i].fields.start_date).getDate()+ '-' + new Date(exprs[i].fields.start_date).getMonth() + '-' +new Date(exprs[i].fields.start_date).getFullYear() + '</li>' +
                        '<li>Price: ' + exprs[i].fields.price + '</li>' +
                        '<span id = "span' + counter + '" class="collapse">' +
                        '<li>Students Needed: ' + exprs[i].fields.num_req + '</li>' +
                        '<li>Current Students: ' + exprs[i].fields.num_current + '</li>' +
                        '<br/>'+
                        '<li>' + exprs[i].fields.details + '</li>' +
                            '<br/>'+
                        '<h5>Requirements: </h5>' +
                        '<li>Age: ' + exprs[i].fields.age_req + '</li>' +
                        '<li>Language: ' + exprs[i].fields.lang_req + '</li>' +
                        '<li>Education: ' + exprs[i].fields.ed_req + '</li>' +
                        '</span>' +
                        '</ul> ' +
                        '<div class="btn-group btn-group-sm" role="group">' +
                        '<button type="button" class="btn-primary" data-toggle="collapse" data-target="#span' + counter + '">See Details</button>' +
                        '</div>' +
                            '</div>'+
                        '</div>' +
                        '</div>'
                    );
                    if (x === 'true') {
                        //If student viewing bid append dynamic buttons with info such as 'bid' 'declined' 'waiting
                        var one = det(exprs[i].fields.ed_req);
                        var two = det(ed);
                        console.log(age);
                        if(age < exprs[i].fields.age_req || lang !== exprs[i].fields.lang_req && exprs[i].fields.lang_req !== 'None' || one > two ){
                            $('#' + i).find('.btn-group').append(
                                '<button type="button" class="btn-danger" value="' + exprs[i].fields.name + '" disabled>Do not meet req</button>' +
                                '</div>')
                        } else if (accepted.includes(exprs[i].pk)) {
                            $('#' + i).find('.btn-group').append(
                                '<button type="button" class="btn-dark" value="' + exprs[i].fields.name + '" disabled>Already accepted</button>' +
                                '</div>')
                        } else if (declined.includes(exprs[i].pk)) {
                            $('#' + i).find('.btn-group').append(
                                '<button type="button" class="btn-danger" value="' + exprs[i].fields.name + '" disabled>Declined</button>' +
                                '</div>')
                        } else if (waiting.includes(exprs[i].pk)){
                            $('#' + i).find('.btn-group').append(
                                '<button type="button" class="btn-warning" value="' + exprs[i].fields.name + '" disabled>Awaiting response</button>' +
                                '</div>')
                        } else {
                            $('#' + i).find('.btn-group').append(
                                '<button id="' + i + '" type="button" class="btn-success" value="' + exprs[i].fields.name + '" >Bid</button>' +
                                '</div>'
                            )
                            apply.push(exprs[i])
                        }
                    }



                }
                counter ++
            }
		 }

function det(ver){
	    //Determine what level of edcuation is 
    // greater than others i.e ensure if expr education set as none a student with school can apply
	    var x = 0;
    switch(ver){
        case 'Postgraduate':
            x = 4;
            break;
        case 'Undergraduate':
            x = 3;
            break;
        case 'College':
            x = 2;
            break;
        case 'School':
            x = 1;
            break;
        case 'None':
            x = 0;
            break;
        default:
            break;
    }
    return x
    }

 function search() {
        var expr = [];
        var filter = document.getElementById('value').value;
        var value = document.getElementById('searchvar').value;
        $.get('/experimenter/getall/', function (data) {
            for (i in data) {
                if (data[i].fields[filter] == value) {
                    expr.push(data[i])
                }
            }
            if(expr.length > 0){
                $( "#val" ).empty();
                load(expr)
            }else{
                $( "#val" ).empty();
                $("#val").append("<h5>No Experiments found with that criteria</h5>")
            }

        });
    }