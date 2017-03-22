$(document).ready(function() {
    ["#from-select", "#to-select"].forEach(function(selectId) {
        $(selectId).selectize({
            sortField: 'text',
            closeOnSelect: true,
            selectOnTab: true,
            items: []
        });
    });
});