
function getFanForm() {
    $('#talent-form').hide()
    $('#fan-form').show()
    $('#fan-button').css('background-color', '#13d664')
    $('#talent-button').css('background-color', '#13d664')
    $('#talent-button').css('background-color', 'black')

    $('#headline').html('CREATE YOUR FAN ACCOUNT')
}
function getTalentForm() {
    $('#fan-form').hide()
    $('#talent-form').show()
    $('#talent-button').css('background-color', '#13d664')
    $('#fan-button').css('background-color', 'black')
    $('#headline').html('CREATE YOUR TALENT ACCOUNT')
}


// ====Fan form validation====
$(document).ready(function () {
    $("#fan-form").validate({
        errorClass: 'errors',
        rules: {
            fanFirstname: {
                required: true,
                minlength: 4,
                maxlength: 20
            },
            fanLastname: {
                required: true,
                minlength: 4,
                maxlength: 20
            },
            fanUsername: {
                required: true,
                minlength: 4,
                maxlength: 20
            },
            fanEmail: {
                required: true,
                minlength: 4,
                maxlength: 40
            },
            fanPassword: {
                required: true,
                minlength: 8,
                maxlength: 20
            },
            fanTimezone: {
                required: true
            },
            fanCheckbox: {
                required: true
            }
        },
        messages: {
            fanFirstname: {
                required: "Please type First Name",
            },
            fanCheckbox: {
                required: "Please check box"
            }
        }
    });
});

//  =====Talent form validation ==== //
$(document).ready(function () {
    $("#talent-form").validate({
        errorClass: 'errors',
        rules: {
            talentFirstname: {
                required: true,
                minlength: 4,
                maxlength: 20
            },
            talentLastname: {
                required: true,
                minlength: 4,
                maxlength: 20
            },
            talentUsername: {
                required: true,
                minlength: 4,
                maxlength: 20
            },
            talentEmail: {
                required: true,
                minlength: 4,
                maxlength: 40
            },
            telentPassword: {
                required: true,
                minlength: 8,
                maxlength: 20
            },
            talentTimezone: {
                required: true
            },
            talentCheckbox: {
                required: true
            }
        },
        messages: {
            talentFirstname: {
                required: "Please type First Name",
            },
            talentCheckbox: {
                required: "Please check box"
            }
        }
    });
});



