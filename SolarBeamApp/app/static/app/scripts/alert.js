//Función para activar alerta con modal, se envía el mensaje a mostrar como parámetro.
function alertType(message) {
        $("#alert .modal-body").html(message);
        $("#alert").modal('show');
    }

