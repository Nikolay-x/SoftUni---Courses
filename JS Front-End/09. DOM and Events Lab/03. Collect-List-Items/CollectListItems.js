function extractText() {
  const uList = Array.from(document.querySelectorAll("#items > li"));
  const result = document.getElementById("result");
  uList.forEach((li) => (result.value += li.textContent + "\n"));
}
