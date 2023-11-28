function showConfirmationDialogWithSweetAlert() {
  const swalWithBootstrapButtons = Swal.mixin({
    customClass: {
      confirmButton: "btn btn-success",
      cancelButton: "btn btn-danger"
    },
    buttonsStyling: false
  });

  swalWithBootstrapButtons.fire({
    title: "Tem certeza?",
    text: "Você não poderá reverter isso!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Sim, exclua!",
    cancelButtonText: "Não, cancele!",
    reverseButtons: true
  }).then((result) => {
    if (result.isConfirmed) {
      swalWithBootstrapButtons.fire({
        title: "Excluindo...",
        icon: "info",
        showConfirmButton: false,
        allowOutsideClick: false
      });
      
      // Submetendo o formulário após um pequeno atraso para permitir que o alerta de exclusão apareça
      setTimeout(() => {
        document.getElementById('delete-form').submit();
      }, 1000); // Ajuste este valor se necessário para permitir que o alerta seja exibido por tempo suficiente
    } else if (result.dismiss === Swal.DismissReason.cancel) {
      swalWithBootstrapButtons.fire({
        title: "Cancelado",
        text: "Seu arquivo imaginário está seguro :)",
        icon: "error"
      });
    }
  });
}
