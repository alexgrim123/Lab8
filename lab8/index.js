$(function () {
    var $from = $('.from');
    var $to = $('.to');
    var $fun = $('.fun');
    var $button = $('.btn');
    var $output = $('.output');

    $button.click(function() {

        var from = parseFloat($from.val());
        var to = parseFloat($to.val());
        const fun = $fun.val();
        var point = [];
        var dx = 0.2;

        var dynamic = setInterval(function () {
            for (var x = from; x <= to; x+=0.1) {
                if (x <= to){
                    var y = eval(fun);
                    point.push([x, y]);
                }
            }

            const points = [{data: point, label: fun}];
            var options = {
                colors: ["#60FF0E"],
                grid:{
                    borderColor: "#FFFFFF",
                }

            };

            $.plot($output, points, options);

                from += dx;
                to += dx;

                clearInterval(dynamic);
            point = [];
        }, 100);


});
});
