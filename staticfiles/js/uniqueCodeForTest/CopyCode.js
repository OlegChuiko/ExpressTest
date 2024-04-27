function copyNumber() {
    var numberElement = document.querySelector(".number");
    var textArea = document.createElement("textarea");
    textArea.value = numberElement.innerText;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand('copy');
    document.body.removeChild(textArea);

    // Показуємо підтвердження про копіювання
    var copyAlert = document.getElementById("copyAlert");
    copyAlert.style.display = "block";

    // Через 3 секунди ховаємо підтвердження
    setTimeout(function() {
        copyAlert.style.display = "none";
    }, 3000);
}