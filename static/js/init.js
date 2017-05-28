(function ($) {
    $(function () {

        $('.button-collapse').sideNav();

    });

    $(function () {

        $('select').material_select();

    });

    $('#favorite').click(function () {
        var fc = $('#favorite_count');
        if ($(this).text() === 'star') {

            $(this).html('star_border');
            fc.html((parseInt(fc.text()) - 1).toString())
        }
        else {
            $(this).html('star');
            fc.html((parseInt(fc.text()) + 1).toString())
        }
    });

})
(jQuery);





