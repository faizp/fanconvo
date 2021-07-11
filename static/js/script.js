
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

//====== fan signup ajax======
function fanSignup() {
    let isvalid = $('#fan-form').valid();
    if (isvalid) {
        let fanFirstname = $('#fanFirstname').val();
        let fanLastname = $('#fanLastname').val();
        let fanUsername = $('#fanUsername').val();
        let fanEmail = $('#fanEmail').val();
        let fanPassword = $('#fanPassword').val();
        let fanTimezone = $('#fanTimezone').val();
        let data = {
            'csrfmiddlewaretoken': '{{ csrf_token }}',
            'fanFirstname': fanFirstname,
            'fanLastname': fanLastname,
            'fanUsername': fanUsername,
            'fanEmail': fanEmail,
            'fanPassword': fanPassword,
            'fanTimezone': fanTimezone
        };
        console.log(data)
        $.ajax({
            url: '/fan-sign-up/',
            method: 'POST',
            data: data,
            dataType: 'json',
            success: function (data) {
                if (data == 'false') {
                    $('#fan-error').show()
                }
                if (data == 'true') {
                    window.alert('Form submitted successfully')
                    window.location.reload()
                }
            }
        })
    }
}

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


// ====talent signup ajax====
function talentSignup() {
    let isvalid = $('#talent-form').valid();
    if (isvalid) {
        let talentFirstname = $('#talentFirstname').val();
        let talentLastname = $('#talentLastname').val();
        let talentUsername = $('#talentUsername').val();
        let talentEmail = $('#talentEmail').val();
        let talentPassword = $('#talentPassword').val();
        let talentTimezone = $('#talentTimezone').val();
        let data = {
            'csrfmiddlewaretoken': '{{ csrf_token }}',
            'talentFirstname': talentFirstname,
            'talentLastname': talentLastname,
            'talentUsername': talentUsername,
            'talentEmail': talentEmail,
            'talentPassword': talentPassword,
            'talentTimezone': talentTimezone
        };
        console.log(data)
        $.ajax({
            url: '/talent-sign-up/',
            method: 'POST',
            data: data,
            dataType: 'json',
            success: function (data) {
                if (data == 'false') {
                    $('#talent-error').show()
                }
                if (data == 'true') {
                    window.alert('Form submitted successfully')
                    window.location.reload()
                }
            }
        })
    }
}
