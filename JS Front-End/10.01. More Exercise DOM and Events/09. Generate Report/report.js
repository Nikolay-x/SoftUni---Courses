function generateReport() {
  const selectedColumns = Array.from(
    document.querySelectorAll("thead > tr > th > input")
  );
  const tableRowsContent = Array.from(document.querySelectorAll("tbody > tr"));
  const output = document.getElementById("output");

  let fieldsToDisplay = {};
  let resultOutput = [...Array(tableRowsContent.length)].map(() => ({}));
  //   console.log(resultOutput);
  output.value = "";

  function addFields() {
    for (let key in fieldsToDisplay) {
      tableRowsContent.forEach((el, index) => {
        let text = el.querySelectorAll("td")[fieldsToDisplay[key]].textContent;
        Object.assign(resultOutput[index], { [key]: text });
      });
    }
  }

  selectedColumns.forEach((el, index) => {
    let [colName, selected] = [el.name, el.checked];
    if (selected) {
      fieldsToDisplay[colName] = index;
    }
  });
  addFields();
  output.value = JSON.stringify(resultOutput);
}
