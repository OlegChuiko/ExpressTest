document.querySelectorAll('.delete-test-button').forEach(button => {
    button.addEventListener('click', function() {
        const testId = this.closest('.edit-buttons').querySelector('input[name="test_id"]').value;
        if (confirm('Ви впевнені, що хочете видалити цей тест?')) {
            this.closest('.delete-test-form').submit();
        }
    });
});