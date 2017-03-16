$gmx(document).ready(function() {
    $.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
    });
    
    $("#region").change(function() {
        if (this.value != 0) {
            getNode(this.value);
        }
        else {
            $("#nodo").prop("disabled", true);
            $("#nodo").html('');
            $("#nodo").append('<option value="0">Selecciona una opci&oacute;n</option>');
        }
    });

    function getNode(idRegion) {
        $.ajax({
            url:'/slp2015/getNode/',
            type: 'POST',
            data : JSON.stringify({"idRegion": idRegion}),
            dataType : 'json',
            csrfmiddlewaretoken : '{{ csrf_token }}',
            success: function (response) {
                $("#nodo").prop("disabled", false);
                if(response.length > 0) {
                    $("#nodo").html('');
                    $("#nodo").append('<option value="0">Selecciona una opci&oacute;n</option>');                    
                    $.each(response, function(key, response) {
                        $("#nodo").append('<option value="'+ response.id +'">'+ response.nombrenodo + '</option>');
                    });
                }
            },
            error: function() {
                alertType("Error. Por favor intenta elegir otra opci&oacute;n.");
            }
        });
    }
});