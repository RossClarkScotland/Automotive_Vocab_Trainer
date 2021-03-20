  $(document).ready(function(){
    //Edge navbar to the right
    $('.sidenav').sidenav({edge: "right"});
    //Initialize collapsible vocabulary cards
    $('.collapsible').collapsible();
    //Initialize topics dropdown menues for add term
    $('select').formSelect();
    //Initialize modals for action confirmation buttons
    $('.modal').modal();
  });