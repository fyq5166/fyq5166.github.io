
$(function() {
    var $tabButtons = $('ul.tab-nav li .button');

    function showTab(href) {
        var $container = $(href).parent();
        $('.tab-pane', $container).removeClass('active').hide();
        $(href).addClass('active').show();
    }

    $tabButtons.each(function() {
        var href = $(this).attr('data-ref');
        if ($(this).hasClass('active')) {
            showTab(href);
        }
    });

    $tabButtons.click(function() {
        var href = $(this).attr('data-ref');

        $('li .active.button', $(this).closest('ul.tab-nav')).removeClass('active');
        $(this).addClass('active');

        showTab(href);

        return false;
    });
});
