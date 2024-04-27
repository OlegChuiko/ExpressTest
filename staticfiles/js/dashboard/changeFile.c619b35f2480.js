function updateFileName() {
    const fileInput = document.getElementById('myInput2');
    const selectedFileName = document.getElementById('selectedFileName');
    selectedFileName.textContent = fileInput.files[0].name;

}
function submitForm() {
    const fileInput = document.getElementById('myInput2');
    if (fileInput.files.length > 0) { 
        document.getElementById('newTest').submit();
    }
}