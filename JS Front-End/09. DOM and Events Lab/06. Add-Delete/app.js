function addItem() {
  const items = document.getElementById("items");
  const newText = document.getElementById("newItemText");
  let newLi = document.createElement("li");
  let newAnchor = document.createElement("a");

  newLi.textContent = newText.value;
  newAnchor.textContent = "[Delete]";
  // newAnchor.setAttribute("href", "#");
  newAnchor.href = "#";
  newAnchor.addEventListener("click", clickHandler);
  newLi.appendChild(newAnchor);
  items.appendChild(newLi);
  newText.value = "";

  function clickHandler(e) {
    const anchor = e.currentTarget;
    anchor.parentElement.remove();
  }
}
