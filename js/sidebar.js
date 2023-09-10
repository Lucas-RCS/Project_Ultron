// Side bar in the Grid screen
// The code is for when you click on the menu button, it activates the class "show-sidebar" and shows the menu

$(function () {

    'use strict';

    $('.js-menu-toggle').click(function (e) {

        var $this = $(this);



        if ($('body').hasClass('show-sidebar')) {
            $('body').removeClass('show-sidebar');
            $this.removeClass('active');
        } else {
            $('body').addClass('show-sidebar');
            $this.addClass('active');
        }

        e.preventDefault();

    });

    // click outisde offcanvas
    $(document).mouseup(function (e) {
        var container = $(".sidebar");
        if (!container.is(e.target) && container.has(e.target).length === 0) {
            if ($('body').hasClass('show-sidebar')) {
                $('body').removeClass('show-sidebar');
                $('body').find('.js-menu-toggle').removeClass('active');
            }
        }
    });



});
const imageContainer = document.getElementById('image-container');
const imageUpload = document.getElementById('image-upload');
const addButton = document.getElementById('add-image');

// Função para adicionar uma imagem à página
function addImage(url) {
    const img = document.createElement('img');
    img.src = url;
    imageContainer.appendChild(img);
}

// Adicionar uma imagem quando o botão for clicado
addButton.addEventListener('click', function () {
    // Executar o upload de imagem quando o botão for clicado
    imageUpload.click();
});

// Lidar com o evento de seleção de arquivo
imageUpload.addEventListener('change', function () {
    const file = imageUpload.files[0];
    if (file) {
        // Criar uma URL temporária para a imagem selecionada
        const imageUrl = URL.createObjectURL(file);
        // Adicionar a imagem à página
        addImage(imageUrl);
    }
});
