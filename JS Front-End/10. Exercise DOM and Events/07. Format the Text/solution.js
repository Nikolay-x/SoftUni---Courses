function solve() {
  const textInput = document.getElementById("input");
  const output = document.getElementById("output");
  let textArrRaw = textInput.value.split(".");
  textArrRaw.splice(textArrRaw.length - 1, 1);

  while (textArrRaw.length > 0) {
    let paragraphText = textArrRaw.splice(0, 3).join(".") + ".";
    let paragraph = document.createElement("p");
    paragraph.textContent = paragraphText;
    output.appendChild(paragraph);
  }
}
