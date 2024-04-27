function toggleExit() {
    var exitButton = document.querySelector('.exit');
    if (exitButton.style.display === 'none') {
        exitButton.style.display = 'flex';
    } else {
        exitButton.style.display = 'none';
    }
}