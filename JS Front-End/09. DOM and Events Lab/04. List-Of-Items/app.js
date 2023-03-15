// function addItem() {
//     const items = document.getElementById("items");
//     const newItemText = document.getElementById("newItemText").value;
//     let newLi = document.createElement("li");
//     newLi.textContent = newItemText;
//     items.append(newLi);
// }

function addItem() {
  const items = document.getElementById("items");
  const newText = document.getElementById("newItemText").value;

  let newLi = document.createElement("li");
  newLi.appendChild(document.createTextNode(newText));
  items.appendChild(newLi);
  document.getElementById("newItemText").value = "";
}
