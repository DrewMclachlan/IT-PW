
    //Click handler for closing an experiment
    $(document).ready(function() {
     $(".btn-outline-secondary").click(function () {
         console.log('test')
         var name = $(this).attr('value');
         $.get('/experimenter/close/',
             {'expr':name},
             function(){
                location.reload()
             }
             )
     })
 })

//Screen user. get info of student and append to pop up model
 $(document).ready(function() {
     $(".btn-outline-info").click(function(){
         $('.modal-body').html('')
         var name = $(this).attr('value');
         console.log(name);
         $.get('/student/displaydetails/',
             {'name': name},
             function(data){
                var obj = JSON.parse(data)
                $('.modal-body').append(
                    '<h6>Anonymous User</h6>' +
                    '<p>Sex:  ' + obj[0].fields.sex + '</p>' +
                    '<p>Age:  ' + obj[0].fields.age + '</p>' +
                '<p>Language:  ' + obj[0].fields.language + '</p>' +
                    '<p>Country:  ' + obj[0].fields.country + '</p>' +
                    '<p>Education:  ' + obj[0].fields.education + '</p>'
                )

             }
         )
     });
 })

    //Accept student bid
 $(document).ready(function() {
     $(".btn-outline-success").click(function () {
         var name = $(this).attr('value');
         var expr = $(this).closest('div').prop('id');
         $(this).parents(":eq(1)").remove();
         $.get('/experimenter/accept/',
             {'expr':expr,'student': name},
             function(){
             document.location.reload(true)

             }
             )
     })
 });


//When an student is accepted the page must be reloaded as if a expr becomes full all other students
    //Are automaticlly declined
    //When using an accordian a realod closed the open card
    //This fucntion stores the value of the open card, when opend in broswer local storage
    //Then after reload, retrevies it and 'reopnes' approprite card.
 $(document).ready(function () {
     $(".btn-link").click(function () {
         localStorage.setItem('collapseItem', $(this).attr('data-target'));
     });
     var collapseItem = localStorage.getItem('collapseItem');
    if (collapseItem) {
       $(collapseItem).collapse('show')
    }
 });

 //Decline student
 $(document).ready(function() {
     $(".btn-outline-danger").click(function () {
         var name = $(this).attr('value')
         var expr = $(this).closest('div').prop('id');
         $(this).parents(":eq(1)").remove();

         $.get('/experimenter/decline/',
             {'expr':expr,'student': name},
             function(){
                 document.location.reload(true)

             }
             )
     })
 });