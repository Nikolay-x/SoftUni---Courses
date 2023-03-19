function editElement(htmlEl, match, replacer) {
  const text = htmlEl.textContent;
  const newText = text.replace(new RegExp(match, "g"), replacer);
  htmlEl.textContent = newText;
}
