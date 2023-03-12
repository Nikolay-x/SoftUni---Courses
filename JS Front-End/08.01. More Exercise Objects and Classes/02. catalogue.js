function catalogueFunc(inputArr) {
  let catalogue = {};
  for (let line of inputArr) {
    let [name, price] = line.split(" : ");
    catalogue[name] = Number(price);
  }
  let sortedCatalogueArr = Object.entries(catalogue).sort(
    (productNameA, productNameB) =>
      productNameA[0].localeCompare(productNameB[0])
  );
  let sortedCatalogue = Object.fromEntries(sortedCatalogueArr);

  let categoryCur = "";
  let category = "";
  let output = [];
  for (key in sortedCatalogue) {
    categoryCur = key[0];
    if (category !== categoryCur) {
      category = categoryCur;
      output.push(category);
    }
    output.push(`  ${key}: ${sortedCatalogue[key]}`);
  }

  console.log(output.join("\n"));
}

catalogueFunc([
  "Appricot : 20.4",
  "Fridge : 1500",
  "TV : 1499",
  "Deodorant : 10",
  "Boiler : 300",
  "Apple : 1.25",
  "Anti-Bug Spray : 15",
  "T-Shirt : 10",
]);

catalogueFunc(["Omlet : 5.4", "Shirt : 15", "Cake : 59"]);
