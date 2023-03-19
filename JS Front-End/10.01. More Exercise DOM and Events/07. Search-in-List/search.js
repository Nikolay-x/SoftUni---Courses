function search() {
  const towns = Array.from(document.querySelector("#towns").children);
  const searchText = document.querySelector("#searchText").value;
  const result = document.querySelector("#result");

  towns.forEach((town) => {
    town.style.textDecoration = "none";
    town.style.fontWeight = "normal";
  });

  let matches = 0;

  towns.forEach((town) => {
    if (town.textContent.includes(searchText)) {
      matches += 1;
      town.style.textDecoration = "underline";
      town.style.fontWeight = "bold";
    }
  });

  result.textContent = `${matches} matches found`;
}
