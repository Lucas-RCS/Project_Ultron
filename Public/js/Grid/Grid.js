const SIZE_CONSTANTS = 30;

class OctagonalArena {
  #baseDocumentElement;
  #gridDocumentElement;
  #contentDocumentElement;
  #interactionDocumentElement;

  #ambient = [];
  #grid = {};

  #card1 = null;
  #card2 = null;

  base_size_w;
  base_size_h;

  #settings = {
    scale: 1,
    cartesiano_size: 10,
    debuggerOn: false,
  };

  /**
   * @constructor
   * @param {Array<any>} options
   * @param {JSON} settings
   */
  constructor(ambient = [], settings = {}) {
    this.#ambient = ambient;
    Object.assign(this.#settings, settings);
  }

  cslick(event, element, x, y) {
    if (!element.classList.contains("active")) {
      this.#ambient.push([x, y]);

      element.classList.add("active");
    } else {
      this.#ambient.splice(
        this.#ambient.findIndex((coord) => coord[0] == x && coord[1] == y),
        1
      );

      element.classList.remove("active");
    }

    console.log(this.#ambient);
  }

  allowDrop(ev) {
    ev.preventDefault();
  }

  drop(ev) {
    ev.preventDefault();
    const cardId = ev.dataTransfer.getData("card");
    var card = document.getElementById(cardId);

    var [x, y] = ev.target.getAttribute("coord").split("-");

    const coord = `${x}-${y}`;

    if (this.#grid[x][y].classList.contains("active")) {
      let base_size = SIZE_CONSTANTS * this.#settings.scale;

      if (card.getAttribute("state") == 1) {
        let cardData = [card, coord];

        if (this.#card1 == card.getAttribute("coord")) this.#card1 = cardData;
        else this.#card2 = cardData;

        card.style.top = this.#grid[x][y].style.top;
        card.style.left = this.#grid[x][y].style.left;
      } else {
        card.setAttribute("state", 1);
        card.setAttribute("coord", coord);

        const cardClone = card.cloneNode(true);

        card.classList.add("deactve");

        cardClone.style.top = this.#grid[x][y].style.top;
        cardClone.style.left = this.#grid[x][y].style.left;
        cardClone.style.width = base_size * 3;
        cardClone.style.height = base_size * 3;

        cardClone.style.paddingTop = this.base_size_h * 0.18;
        cardClone.style.paddingLeft = this.base_size_w * 0.48;

        this.#contentDocumentElement.appendChild(cardClone);

        this.Card = [cardClone, coord];
      }
    } else
      alert("Não é possível incluir personagens em coordenadas desativadas.");
  }

  getAmbient() {
    return this.#ambient.map((coord) => {
      let [x, y] = coord;

      return `${x}-${y}`;
    });
  }

  makePath(paths) {
    this.#card1[0];

    console.log(paths);

    let i = 0;

    for (const path of paths) {
      setTimeout(() => {
        let [x, y] = path.split("-");

        this.#card1[0].style.top = this.#grid[x][y].style.top;
        this.#card1[0].style.left = this.#grid[x][y].style.left;

        this.#card1[1] = [x, y];
      }, i * 1150);

      i++;
    }
  }

  get Card() {
    return [this.#card1, this.#card2];
  }

  set Card(card) {
    let cardBar = document.getElementById("cardBar");

    if (this.#card1 == null) {
      this.#card1 = card;

      cardBar.innerHTML += `
      <div class="cardLine">
        <img src="./Public/img/coroa.png">
        <p>${card[0].getAttribute("alt")}</p>
      </div>
      `;
    } else {
      this.#card2 = card;

      cardBar.innerHTML += `
      <div class="cardLine">
        <img src="./Public/img/ciclo.png">
        <p>${card[0].getAttribute("alt")}</p>
      </div>
      `;
    }
  }

  createGrid() {
    const root = document.documentElement;

    var base = document.getElementById("base");
    this.#baseDocumentElement = base;

    var content = document.createElement("div");
    content.id = "content";
    this.#contentDocumentElement = content;

    var grid = document.createElement("div");
    grid.id = "grid";
    this.#gridDocumentElement = grid;

    base.appendChild(content);
    base.appendChild(grid);

    const ambient = this.#ambient;

    let { scale, cartesiano_size } = this.#settings;

    let base_size = SIZE_CONSTANTS * scale;

    cartesiano_size += 2;

    let base_size_w = base_size;
    let base_size_h = Math.round((Math.sqrt(3) * (base_size * 2)) / 2);

    this.base_size_w = base_size_w;
    this.base_size_h = base_size_h;

    let hex_width = base_size_w * 4;
    let hex_height = base_size_h * 2;

    root.style.setProperty("--middle-w", base_size_w * 2 + "px");
    root.style.setProperty("--middle-h", hex_height + "px");
    root.style.setProperty("--hex-b", base_size_w + "px");
    root.style.setProperty("--hex-b-c", base_size_h + "px");

    let width = hex_width * cartesiano_size;
    let height = hex_height * cartesiano_size;

    grid.style.width = width + (base_size_h + 5) * 2 + "px";
    grid.style.height = height + base_size_w * 10 + "px";

    content.style.width = grid.style.width;
    content.style.height = grid.style.height;

    let y = base_size_h * 2;
    let x = base_size_w * 5;

    for (let i = 1; i <= cartesiano_size; i++) {
      this.#grid[i] = {};

      let hex_row = document.createElement("div");
      hex_row.classList = "hex-row";

      let v = true;

      for (let e = 1; e <= cartesiano_size; e++) {
        let hex = document.createElement("div");

        let isActive = ambient.findIndex(
          (coord) => coord[0] == i && coord[1] == e
        );

        hex.classList = `hex ${isActive == -1 ? "" : "active"}`;
        hex.setAttribute("id", `${i}-${e}`);

        hex.onclick = (event) => {
          this.cslick(event, hex, i, e);
        };

        hex.style.minHeight = hex_height;
        hex.style.minWidth = hex_width;

        hex.style.top = v ? y : y + base_size_h + 2 + "px";
        hex.style.left = x + "px";

        let left = document.createElement("div");
        left.classList = "left";

        let middle = document.createElement("div");
        middle.classList = "middle";

        let right = document.createElement("div");
        right.classList = "right";

        let span = document.createElement("span");
        span.className = "coord";
        span.innerHTML = `${i} - ${e}`;
        middle.appendChild(span);

        middle.ondrop = (e) => {
          this.drop(e);
        };
        middle.ondragover = (e) => {
          this.allowDrop(e);
        };

        hex.appendChild(left);
        hex.appendChild(middle);
        hex.appendChild(right);

        hex_row.appendChild(hex);

        hex.setAttribute("coord", `${i}-${e}`);
        span.setAttribute("coord", `${i}-${e}`);
        left.setAttribute("coord", `${i}-${e}`);
        middle.setAttribute("coord", `${i}-${e}`);
        right.setAttribute("coord", `${i}-${e}`);

        x += base_size_w * 3;
        x += 3;
        v = !v;

        this.#grid[i][e] = hex;
      }

      x = base_size_w * 5;
      y += base_size_h * -1 + base_size_h * 3;

      y += 4;

      grid.appendChild(hex_row);
    }
  }
}
