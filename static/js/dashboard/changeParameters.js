function enableInput(inputId) {
    const inputElement = document.getElementById(inputId);
    if (inputElement) {
        inputElement.removeAttribute("disabled");
        inputElement.focus();
    }
}

let inputActivated1 = false;
document.addEventListener("DOMContentLoaded", function() {
    const activateBtn = document.getElementById("activateBtn1");
    const myInput = document.getElementById("myInput1");
    const form = document.getElementById('newName')

    activateBtn.addEventListener("click", function() {
        if (!inputActivated1) {
            myInput.removeAttribute("disabled");
            myInput.focus();
            inputActivated1 = true;
        } else {
            inputActivated1 = false;
            form.submit();
        }
    });

    myInput.addEventListener("blur", function() {
        myInput.setAttribute("disabled", true);
    });
});

let inputActivated3 = false;
document.addEventListener("DOMContentLoaded", function() {
    const activateBtn = document.getElementById("activateBtn3");
    const myInput = document.getElementById("myInput3");
    const form = document.getElementById('newDuration')

    activateBtn.addEventListener("click", function() {
        if (!inputActivated3) {
            myInput.removeAttribute("disabled");
            myInput.focus();
            inputActivated3 = true;
        } else {
            inputActivated3 = false;
            form.submit();
        }
    });

    myInput.addEventListener("blur", function() {
        myInput.setAttribute("disabled", true);
    });
});  