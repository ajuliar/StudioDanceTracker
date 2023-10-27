const button = document.querySelector("#submit")
button.addEventListener ('click', () => {
    const formEnroll = {
        get_student: document.querySelector("#student-selector").value,
        get_class: document.querySelector("#class-selector").value,
    };

    fetch("/enroll-students", {
        method: 'POST',
        body: JSON.stringify(formEnroll),
        headers: {
            'Content-type': 'application/json',
        },
    })
        .then((response) => response.json())
        .then((responseJson) => {
            alert(responseJson.status);
        });

});