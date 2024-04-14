// Функція для збереження вибраних відповідей у локальному сховищі
function saveSelectedAnswer(questionId, selectedAnswerId) {
    localStorage.setItem(questionId, selectedAnswerId);
}

// Функція для отримання збережених відповідей з локального сховища
function loadSelectedAnswer(questionId) {
    return localStorage.getItem(questionId);
}

// Підключення до всіх радіо кнопок та прапорців
const inputs = document.querySelectorAll('input[type="radio"]');

// Додавання обробника подій для кожного варіанту відповіді
inputs.forEach(input => {
    input.addEventListener('change', function() {
        const questionId = this.closest('.test-content, .test-content2').getAttribute('id');
        const selectedAnswerId = this.getAttribute('id');
        saveSelectedAnswer(questionId, selectedAnswerId);
    });
});

// Відновлення збережених відповідей при завантаженні сторінки
window.addEventListener('load', function() {
    inputs.forEach(input => {
        const questionId = input.closest('.test-content, .test-content2').getAttribute('id');
        const savedAnswerId = loadSelectedAnswer(questionId);
        if (savedAnswerId === input.getAttribute('id')) {
            input.checked = true;
        }
    });
});



