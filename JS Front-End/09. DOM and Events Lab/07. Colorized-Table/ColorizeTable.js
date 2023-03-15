// function colorize() {
//   const rows = Array.from(document.querySelectorAll("tr:nth-of-type(2n)"));
//   rows.forEach((tr) => (tr.style.backgroundColor = "teal"));
// }

function colorize() {
  const rows = Array.from(document.querySelectorAll("tr:not(:first-child)"));
  for (let i = 0; i < rows.length; i++) {
    if (i % 2 === 0) {
      rows[i].style.backgroundColor = "teal";
    }
  }
}
