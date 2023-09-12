// Obtém o modal e os elementos de fechamento
const modal = document.getElementById('myModal');
const openModalIcon = document.getElementById('openModal');
const closeModalIcon = document.getElementById('closeModal');

// Abre o modal quando o ícone é clicado
openModalIcon.addEventListener('click', function () {
    modal.style.display = 'block';
});

// Fecha o modal quando o ícone de fechamento é clicado
closeModalIcon.addEventListener('click', function () {
    modal.style.display = 'none';
});

// Fecha o modal quando o usuário clica fora dele
window.addEventListener('click', function (event) {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});