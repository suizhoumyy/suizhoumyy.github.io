// 全屏图片
(function() {
    var body = $('body');
    var imgdiv = $('#img-view');

    imgdiv.click(function() {
        body.css('max-height', 'none');
        body.css('overflow', 'auto');

        imgdiv.hide();
    });

    function view_image(e) {
        $('#img-view img').attr('src', e.src);
        body.css('max-height', window.innerHeight);
        body.css('overflow', 'hidden');
        imgdiv.show();
    }

    $('body img').click(function(e) {
        view_image(this);
    });
})();
