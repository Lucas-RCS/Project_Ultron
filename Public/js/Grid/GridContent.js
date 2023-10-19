export default class {
  name = "";
  HP = 15;
  #img = 0;
  #imgPosibilities = {
    1: {
      name: "default",
      src: "../../img/cards/default.png",
    },
  };

  set img(imageId) {
    if (this.#imgPosibilities.hasOwnProperty(imageId)) this.#img = imageId;
    else this.#img = 0;
  }
}
