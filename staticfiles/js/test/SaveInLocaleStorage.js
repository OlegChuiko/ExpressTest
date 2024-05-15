function saveUserAnswers() {
    var answers = document.querySelectorAll('input[type=radio]:checked');
    var userAnswers = {};
    answers.forEach(function(answer) {
        if (answer.value !== "INCORRECTTTTTT#@!") {
            userAnswers[answer.name] = answer.value;
        }

    });
    localStorage.setItem('userAnswers', JSON.stringify(userAnswers));
}

function restoreUserAnswers() {
    var userAnswers = localStorage.getItem('userAnswers');
    if (userAnswers) {
        userAnswers = JSON.parse(userAnswers);
        Object.keys(userAnswers).forEach(function(key) {
            var input = document.querySelector('input[name=' + key + '][value="' + userAnswers[key] + '"]');
            if (input) {
                input.checked = true;
            }
        });
    }
}

restoreUserAnswers();

window.addEventListener('beforeunload', function(event) {
    localStorage.removeItem('userAnswers');
    saveUserAnswers();
});
