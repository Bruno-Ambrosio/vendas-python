function showConfirmationDialog() {
    var isConfirmed = confirm("Tem certeza de que deseja excluir este cliente?");
    if (isConfirmed) {
        document.getElementById('delete-form').submit();
    }
}