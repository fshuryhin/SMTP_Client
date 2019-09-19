function sendMail() 
{
    $('#message').html();
    
    formData = $('#sendmail').serializeArray();

    $.ajax({
        url: 'send/',
        type: 'POST',
        //dataType : "json",
        //async: false,
        data: formData,
        success: function(answer) {
            //alert (answer.message);
            $('#message').html(answer.message)

            if(!$.isEmptyObject(answer.errList)) {
                $('#message').append('<div>Error List:</div>');
                $('#message').append('<table>');

                $.each(answer.errList, function(key, value) {
                    $('#message').append(
                        '<tr>' +
                            '<td class="td">' + key + '</td>' + 
                            '<td class="td">' + value + '</td>' +
                        '</tr>'
                    );
                });

                $('#message').append('</table>');
            }
        }
    });
}

function setSettings() 
{
    $('#smptmessage').html();

    formData = $('#setsettings').serializeArray();
    
    $.ajax({
        url: 'settings/',
        type: 'post',
        //dataType : "json",
        //async: false,
        data: formData,
        success: function(answer) {
            $('#smptmessage').html(answer);
        }
    });
}

$(function() {
    $('#toggle').on('click', function() {
        $('.toggle').slideToggle();
    });
});