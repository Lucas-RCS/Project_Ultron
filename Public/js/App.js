const Arena = new OctagonalArena(
  [
    [14, 14],
    [13, 14],
    [12, 14],
    [11, 14],
    [15, 14],
    [16, 14],
    [17, 14],
    [15, 15],
    [15, 13],
    [16, 15],
    [15, 16],
    [14, 16],
    [13, 15],
    [13, 13],
    [14, 12],
    [15, 12],
    [16, 13],
    [17, 15],
    [16, 16],
    [16, 17],
    [15, 17],
    [12, 16],
    [12, 15],
    [12, 13],
    [12, 12],
    [13, 11],
    [14, 11],
    [15, 11],
    [16, 11],
    [16, 12],
    [17, 13],
    [18, 14],
    [18, 15],
    [17, 16],
    [17, 17],
    [15, 18],
    [14, 18],
    [13, 18],
    [12, 18],
    [12, 17],
    [11, 16],
    [11, 15],
    [10, 14],
    [11, 13],
    [11, 12],
    [12, 11],
    [12, 10],
    [13, 10],
    [14, 10],
    [17, 12],
    [18, 13],
    [14, 19],
    [15, 19],
    [14, 9],
    [15, 9],
    [16, 19],
    [18, 16],
    [19, 15],
    [19, 14],
    [19, 13],
    [18, 12],
    [18, 11],
    [17, 10],
    [17, 9],
    [16, 9],
    [13, 9],
    [11, 10],
    [11, 11],
    [10, 12],
    [10, 13],
    [9, 14],
    [10, 15],
    [10, 16],
    [11, 17],
    [11, 18],
    [12, 19],
    [13, 19],
    [8, 14],
    [7, 14],
    [8, 15],
    [9, 15],
    [8, 16],
    [9, 16],
    [10, 17],
    [10, 18],
    [11, 19],
    [10, 19],
    [11, 20],
    [10, 20],
    [12, 20],
    [12, 21],
    [11, 21],
    [13, 21],
    [13, 20],
    [14, 21],
    [14, 20],
    [15, 20],
    [16, 20],
    [17, 20],
    [18, 19],
    [19, 17],
    [19, 16],
    [20, 15],
    [20, 14],
    [20, 13],
    [19, 12],
    [19, 11],
    [18, 10],
    [18, 9],
    [17, 8],
    [16, 8],
    [15, 8],
    [14, 8],
    [13, 8],
    [12, 8],
    [11, 8],
    [9, 12],
    [9, 13],
    [15, 21],
    [16, 21],
    [17, 21],
    [18, 21],
    [18, 20],
    [19, 19],
    [19, 18],
    [20, 17],
    [20, 16],
    [21, 15],
    [21, 14],
    [21, 13],
    [20, 12],
    [19, 9],
    [18, 8],
    [18, 7],
    [17, 7],
    [16, 7],
    [15, 7],
    [14, 7],
    [13, 7],
    [13, 7],
    [12, 7],
    [11, 7],
    [10, 8],
    [10, 9],
    [9, 11],
    [8, 12],
    [8, 13],
    [14, 22],
    [15, 22],
    [13, 22],
    [14, 23],
    [15, 23],
    [13, 6],
    [14, 6],
    [15, 6],
    [14, 5],
    [15, 5],
    [20, 9],
    [20, 10],
    [21, 11],
    [21, 9],
    [21, 10],
    [21, 17],
    [20, 18],
    [20, 19],
    [21, 19],
    [21, 18],
    [8, 17],
    [9, 19],
    [7, 18],
    [8, 19],
    [9, 9],
    [8, 10],
    [8, 11],
    [8, 9],
    [7, 10],
    [11, 6],
    [10, 6],
    [10, 7],
    [9, 6],
    [11, 5],
    [10, 21],
    [10, 5],
    [11, 22],
    [10, 22],
    [11, 23],
    [10, 23],
    [9, 22],
    [17, 22],
    [19, 21],
    [18, 22],
    [18, 23],
    [19, 22],
    [19, 23],
    [19, 7],
    [17, 6],
    [18, 6],
    [19, 6],
    [18, 5],
    [19, 5],
  ],
  {
    cartesiano_size: 25,
    scale: 0.6,
  }
);

Arena.createGrid();

function drag(ev) {
  if (!ev.target.classList.contains("deactive"))
    ev.dataTransfer.setData("card", ev.target.id);
}

function construirURLComParametros(url, parametros) {
  var partes = [];
  for (var chave in parametros) {
    if (parametros.hasOwnProperty(chave)) {
      partes.push(
        encodeURIComponent(chave) + "=" + encodeURIComponent(parametros[chave])
      );
    }
  }
  return url + "?" + partes.join("&");
}

function submit() {
  let radio;

  els = document.getElementsByName("radio-group");

  for (var i = 0; i < els.length; i++) if (els[i].checked) radio = els[i].value;

  const limited_depth = document.getElementById("limited-depth") ?? 1;

  let cards = Arena.Card;

  if (cards[0] == null || cards[1] == null)
    alert(
      "Para iniciar o combate, é necessário inserir pelo menos dois cards na arena."
    );
  else {
    var xhr = new XMLHttpRequest();

    // Configura a função de callback para quando a resposta for recebida
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        var resposta = JSON.parse(xhr.responseText);

        Arena.makePath(resposta);

        console.log(resposta);
      }
    };

    if (radio == "profundidadelimit") radio += "/" + limited_depth;

    // Configura a requisição
    xhr.open(
      "GET",
      construirURLComParametros(`./${radio}`, {
        ambient: Arena.getAmbient(),
        beginning: cards[0][1],
        destination: cards[1][1],
      }),
      true
    );

    // Envia a requisição
    xhr.send();
  }
}

const modal = document.getElementById("myModal");
const openModalIcon = document.getElementById("openModal");
const closeModalIcon = document.getElementById("closeModal");
const svgObject = document.getElementById("svgObject");
const modalContent = document.getElementById("modalContent");
const svg = document.getElementById("svg");
const hr = document.getElementById("hr");
const Btnstart = document.getElementById("Btn");

openModalIcon.addEventListener("click", function () {
  modal.style.display = "flex";

  setTimeout(function () {
    svgObject.style.opacity = "0";
  }, 2000); // 2000ms = 2 secon

  setTimeout(function () {
    svgObject.style.display = "none";
    modalContent.style.display = "block";
    modalContent.classList.add("fade-in-stagger");
    svg.style.display = "none";
    hr.style.display = "block";
    hr.classList.add("fade-in-stagger");
    Btnstart.style.display = "block";
    Btnstart.classList.add("fade-in-stagger");
    closeModalIcon.style.display = "block";
    closeModalIcon.classList.add("fade-in-stagger");
  }, 2200);
});

closeModalIcon.addEventListener("click", function () {
  modal.style.display = "none";
  svgObject.style.opacity = "1";
  svgObject.style.display = "block";
  modalContent.style.display = "none";
  svg.style.display = "flex";
  hr.style.display = "none";
  Btnstart.style.display = "none";
  closeModalIcon.style.display = "none";
});

var menuOptions = document.querySelectorAll(".iconsMenu");
var mainContent = document.querySelectorAll(".main > div");

function showContent(optionId) {
  mainContent.forEach(function (content) {
    content.style.display = "none";
  });
  var contentToShow = document.getElementById(optionId + "Content");
  if (contentToShow) {
    contentToShow.style.display = "flex";
  }
}

menuOptions.forEach(function (option) {
  option.addEventListener("click", function () {
    var optionId = this.id;
    showContent(optionId);
  });
});

showContent("option1");
