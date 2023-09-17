const n = 15;
const store = {};
var html = document.getElementById("content");

function cslick(event, i, e) {
    if (store[i] == undefined) store[i] = [];
    store[i][e] = true;



    // event.target.classList.add("on");

    // console.log(i, e);

    document.getElementById(`${i}-${e}`).classList.add("on");
}

for (let i = 1; i < n; i++) {

    let hex_row = document.createElement("div");
    hex_row.classList = "hex-row";

    let v = true;

    for (let e = 1; e < n + 2; e++) {

        let hex = document.createElement("div");
        hex.classList = `hex ${v ? "" : "even"}`;
        hex.setAttribute("id", `${i}-${e}`);
        hex.onclick = (event) => { cslick(event, i, e) };

        let left = document.createElement("div");
        left.classList = "left";

        let middle = document.createElement("div");
        middle.classList = "middle";

        middle.innerHTML = `${i}-${e}`;

        let right = document.createElement("div");
        right.classList = "right";

        hex.appendChild(left);
        hex.appendChild(middle);
        hex.appendChild(right);

        hex_row.appendChild(hex);

        v = !v;
    }

    html.appendChild(hex_row)
}


const modal = document.getElementById('myModal');
const openModalIcon = document.getElementById('openModal');
const closeModalIcon = document.getElementById('closeModal');
const svgObject = document.getElementById('svgObject');
const modalContent = document.getElementById('modalContent');
const svg = document.getElementById('svg');
const hr = document.getElementById('hr');
const Btnstart = document.getElementById('Btn');


openModalIcon.addEventListener('click', function () {
    modal.style.display = 'flex';

    setTimeout(function () {
        svgObject.style.opacity = "0";
    }, 2000); // 2000ms = 2 seconds

    setTimeout(function () {
        svgObject.style.display = "none";
        modalContent.style.display = "block";
        modalContent.classList.add('fade-in-stagger');
        svg.style.display = "none";
        hr.style.display = "block";
        hr.classList.add('fade-in-stagger');
        Btnstart.style.display = "block";
        Btnstart.classList.add('fade-in-stagger');
        closeModalIcon.style.display = "block";
        closeModalIcon.classList.add('fade-in-stagger');
    }, 2200);
});

closeModalIcon.addEventListener('click', function () {
    modal.style.display = 'none';
    svgObject.style.opacity = "1";
    svgObject.style.display = "block";
    modalContent.style.display = "none";
    svg.style.display = "flex";
    hr.style.display = "none";
    Btnstart.style.display = "none";
    closeModalIcon.style.display = "none";
});
