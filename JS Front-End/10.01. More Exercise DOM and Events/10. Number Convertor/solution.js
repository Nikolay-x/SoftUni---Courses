function solve() {
  const options = document.querySelector("#selectMenuTo");
  const input = document.querySelector("#input");
  const result = document.querySelector("#result");
  const btn = document.querySelector("button");

  btn.addEventListener("click", clickHandler);

  const optionsMenu = {
    Binary: "binary",
    Hexadecimal: "hexadecimal",
  };

  for (let key in optionsMenu) {
    let option = document.createElement("option");
    option.value = optionsMenu[key];
    option.text = key;
    options.appendChild(option);
  }

  function clickHandler() {
    let [number, selected] = [Number(input.value), options.value];
    if (selected === "binary") {
      result.value = number.toString(2);
    } else if (selected === "hexadecimal") {
      result.value = number.toString(16).toLocaleUpperCase();
    }
  }
}
