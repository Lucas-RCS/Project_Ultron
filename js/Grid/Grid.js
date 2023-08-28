import Content from "./Content";

/**
 * @class
 * @name HexagonalArena
 *
 * @property {HTMLElement} baseDocumentElement Stores the element where all structures are placed
 *
 * @property {HTMLElement} gridDocumentElement Stores the element where the hexagonal grid are placed
 * @property {HTMLElement} contentDocumentElement Stores the element where the cards present in the grid are placed
 * @property {HTMLElement} interactionDocumentElement Stores the element where the structures with the interactions events are placed
 *
 * @property {Array<HTMLElement>} ambientMatrix Matrix with the elements of grid
 * @property {Array<Content>} cardsMatrix Matrix with cards that are in the grid
 * @property {Array<HTMLElement>} cellsMatrix Matrix com os elementos interativos da grade
 *
 * @property {JSON} settings Json with build process settings
 */
export default class {
  #baseDocumentElement;

  #gridDocumentElement;
  #contentDocumentElement;
  #interactionDocumentElement;

  #ambientMatrix = [];
  #cardsMatrix = [];
  #cellsMatrix = [];

  #settings = {
    sixe: [15, 15],
    debuggerOn: false,
  };

  /**
   * @constructor
   * @param {Array<any>} options
   * @param {JSON} settings
   */
  constructor(settings = {}, initAmbientMatrix = []) {
    Object.assign(this.#settings, settings);
    this.#ambientMatrix = initAmbientMatrix;
  }
}

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
    hex.onclick = (event) => {
      cslick(event, i, e);
    };

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

  html.appendChild(hex_row);
}

// document.getElementById("content").innerHTML = html;;
