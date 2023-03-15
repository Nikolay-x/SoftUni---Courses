function deleteByEmail() {
  const email = document.getElementsByName("email")[0].value;
  const cells = document.querySelectorAll("#customers tr td:nth-child(even)");
  const result = document.getElementById("result");

  for (const cell of cells) {
    if (cell.textContent === email) {
      let row = cell.parentNode;
      row.parentNode.removeChild(row);
      result.textContent = "Deleted";
      return;
    }
    result.textContent = "Not found.";
  }
}
