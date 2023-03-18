function solve() {
  document.querySelector("#searchBtn").addEventListener("click", onClick);

  function onClick() {
    const inputSearch = document.querySelector("#searchField");
    const rows = Array.from(
      document.querySelectorAll("body > table > tbody > tr")
    );

    let searchString = inputSearch.value;

    for (const row of rows) {
      if (row.classList.contains("select")) {
        row.classList.remove("select");
      }

      if (row.textContent.includes(searchString)) {
        row.classList.add("select");
      }
    }
    inputSearch.value = "";
  }
}
