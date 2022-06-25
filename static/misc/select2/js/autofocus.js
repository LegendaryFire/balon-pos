// This script allows for autofocusing on the select2 textbox when opened. May only be needed for remote data sources.
$(document).on('select2:open', () => {
    document.querySelector('.select2-search__field').focus();
});