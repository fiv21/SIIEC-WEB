$(document).ready(function(){
 
        $('table').on('mousedown', 'input', function(e){
      var id_seleccionado= $(this).attr('value');
      $("#id_pac_ventricular").val(id_seleccionado);

// alert(id_seleccionado)
  });

});