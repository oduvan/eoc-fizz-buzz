//Dont change it
requirejs(['ext_editor_io', 'jquery_190'],
    function (extIO, $) {
        var $tryit;

        var io = new extIO({
            functions: {
                js: 'fizzBuzz',
                python: 'fizz_buzz'
            },
            tryit:function (this_e) {
                $tryit = this_e.extSetHtmlTryIt(this_e.getTemplate('tryit')).find(".tryit-content");
                $tryit.find('.bn-check').click(function (e) {
                    e.preventDefault();
                    var $input = $tryit.find(".tool .input-number");
                    var data = Number($input.val());
                    if (!isNaN(data)) {
                        data = Number(data);
                    }
                    this_e.extSendToConsoleCheckiO(data);
                    e.stopPropagation();
                    return false;
                });

                $tryit.find('.bn-random').click(function (e) {
                    e.preventDefault();
                    var numb = Math.floor(Math.random() * 10000);
                    $tryit.find(".tool .input-number").val(numb);
                    return false;
                });

            },
            retConsole: function (ret) {
                $tryit.find(".checkio-result").html("Your Result<br>" + ret);
            }
        });
        io.start();


    }
);
