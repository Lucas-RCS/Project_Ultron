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

    // document.getElementById("content").innerHTML = html;;