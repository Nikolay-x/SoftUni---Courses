function solve() {
  const [btnCheck, btnClear] = Array.from(document.querySelectorAll("button"));
  const tableRows = Array.from(document.querySelectorAll("tbody > tr"));
  const table = document.querySelector("table");
  const output = document.querySelector("#check > p");

  let array = [];

  btnCheck.addEventListener("click", check);
  btnClear.addEventListener("click", clear);
  let isCorrect = true;

  function checkColumns() {
    for (let i = 0; i < array.length; i++) {
      let row = array[i];
      let col = array.map((row) => row[i]);
      if (
        col.length !== new Set(col).size ||
        row.length !== new Set(row).size
      ) {
        isCorrect = false;
        break;
      }
    }
  }

  function check() {
    for (let items of tableRows) {
      let row = Array.from(items.querySelectorAll("td > input"));
      let rowData = [];
      for (let item of row) {
        let number = Number(item.value);
        rowData.push(number);
      }
      array.push(rowData);
    }

    checkColumns();
    if (isCorrect) {
      table.style.border = "2px solid green";
      output.textContent = "You solve it! Congratulations!";
      output.style.color = "green";
    } else {
      table.style.border = "2px solid red";
      output.textContent = "NOP! You are not done yet...";
      output.style.color = "red";
    }
  }

  function clear() {
    tableRows.forEach((x) => {
      Array.from(x.querySelectorAll("td > input")).forEach((y) => {
        y.value = "";
      });
    });
    table.style.border = "";
    output.textContent = "";
    output.style.color = "";
  }
}
