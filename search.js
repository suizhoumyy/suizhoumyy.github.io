function get_result(query) {
    var terms = [ 
        {% for term in terms %}{{ term|safe }},{% endfor %}
    ];
    var head = '<div class="weui_cells weui_cells_access">';
    var tail = '</div>';
    var template = '\
        <a class="weui_cell" href="{URL}">\
            <div class="weui_cell_bd weui_cell_primary">\
                <p>{NAME}</p>\
            </div>\
            <span class="weui_cell_ft"></span>\
        </a>\
    ';
    var matches = [];

    // 比较函数
    var matchComparator = function matchComparator(m1, m2) {
        return (m2[0].score - m1[0].score != 0) ? m2[0].score - m1[0].score : m1[0].term.length - m2[0].term.length;
    };

    // 贪婪匹配
    for (var i = terms.length - 1; i >= 0; i--) {
        var match = fuzzy(terms[i][0], query);
        if (match.score > 0) {
            var temp = [match, terms[i][1], terms[i][2]];
            matches.push(temp);
        }
    };
    if (matches.length == 0) {
        return '\
                <div class="weui_cells weui_cells_access">\
                    <a class="weui_cell" href="javascript:;">\
                        <div class="weui_cell_bd weui_cell_primary">\
                            <p>无结果</p>\
                        </div>\
                        <span class="weui_cell_ft"></span>\
                    </a>\
                </div>\
        ';
    };
    // 排序
    matches.sort(matchComparator);
    var result = head;
    // 最多五个结果
    for (var i = 0; i <= matches.length - 1 && i<= 4; i++) {
        var temp = template.replace('{NAME}', matches[i][1])
        result += temp.replace('{URL}', matches[i][2])
    };
    result += tail;
    return result;
};

(function() {
    $('#container').on('focus', '#search_input', function() {
        var $weuiSearchBar = $('#search_bar');
        $weuiSearchBar.addClass('weui_search_focusing');
    }).on('blur', '#search_input', function() {
        var $weuiSearchBar = $('#search_bar');
        $weuiSearchBar.removeClass('weui_search_focusing');
        if ($(this).val()) {
            $('#search_text').hide();
        } else {
            $('#search_text').show();
        }
    }).on('input', '#search_input', function() {
        var $searchShow = $("#search_show");

        if ($(this).val()) {
            $("#search_show")[0].innerHTML = get_result($(this).val());
            $searchShow.show();
        } else {
            $searchShow.hide();
        }
    }).on('touchend', '#search_cancel', function() {
        $("#search_show").hide();
        $('#search_input').val('');
    }).on('touchend', '#search_clear', function() {
        $("#search_show").hide();
        $('#search_input').val('');
    });
})();
