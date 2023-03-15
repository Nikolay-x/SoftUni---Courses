function sumTable() {
  const tableRows = Array.from(
    document.querySelectorAll("body > table > tbody > tr:not(:first-child)")
  );
  const sum = document.getElementById("sum");

  let totalSum = 0;

  for (let i = 0; i < tableRows.length - 1; i++) {
    totalSum += Number(tableRows[i].children[1].textContent);
  }
  sum.textContent = totalSum;
}

// function sumTable() {
//   const prices = document.querySelectorAll("tr td:nth-of-type(2)");
//   const sum = document.getElementById("sum");

//   let totalPrice = Array.from(prices).reduce((a, x) => {
//     let currPrice = Number(x.textContent) || 0;
//     return a + currPrice;
//   }, 0);

//   sum.textContent = totalPrice;
// }
