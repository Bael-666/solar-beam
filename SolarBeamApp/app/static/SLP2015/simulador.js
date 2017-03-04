$gmx(document).ready(function() {
    $("#region").change(function() {
        getNode(this.value);
    });

    function getNode(idRegion) {
        $.ajax({
            url:'/SLP15/getRegion.py',
            type: 'post',
            data : idRegion,
            success: function (response) {
                alert("se envió");
            }
        });
    }
});