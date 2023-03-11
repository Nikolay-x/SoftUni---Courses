// function store(storeArr, orderArr) {
//   let storeProducts = {};
//   for (let i = 0; i < storeArr.length; i += 2) {
//     let product = storeArr[i];
//     let qty = storeArr[i + 1];
//     storeProducts[product] = Number(qty);
//   }
//   for (let i = 0; i < orderArr.length; i += 2) {
//     let product = orderArr[i];
//     let qty = orderArr[i + 1];
//     if (storeProducts.hasOwnProperty(product)) {
//       storeProducts[product] += Number(qty);
//     } else {
//       storeProducts[product] = Number(qty);
//     }
//   }
//   for (const key in storeProducts) {
//     console.log(`${key} -> ${storeProducts[key]}`);
//   }
// }

function storeDemo(storeArr, orderArr) {
  let combined = [...storeArr, ...orderArr];
  let storeProducts = {};
  for (let i = 0; i < combined.length; i += 2) {
    let product = combined[i];
    let qty = Number(combined[i + 1]);
    if (storeProducts.hasOwnProperty(product)) {
      storeProducts[product] += qty;
    } else {
      storeProducts[product] = qty;
    }
  }
  for (const key in storeProducts) {
    console.log(`${key} -> ${storeProducts[key]}`);
  }
}

// store(
//   ["Chips", "5", "CocaCola", "9", "Bananas", "14", "Pasta", "4", "Beer", "2"],
//   ["Flour", "44", "Oil", "12", "Pasta", "7", "Tomatoes", "70", "Bananas", "30"]
// );

// store(
//   ["Salt", "2", "Fanta", "4", "Apple", "14", "Water", "4", "Juice", "5"],
//   ["Sugar", "44", "Oil", "12", "Apple", "7", "Tomatoes", "7", "Bananas", "30"]
// );

storeDemo(
  ["Chips", "5", "CocaCola", "9", "Bananas", "14", "Pasta", "4", "Beer", "2"],
  ["Flour", "44", "Oil", "12", "Pasta", "7", "Tomatoes", "70", "Bananas", "30"]
);

storeDemo(
  ["Salt", "2", "Fanta", "4", "Apple", "14", "Water", "4", "Juice", "5"],
  ["Sugar", "44", "Oil", "12", "Apple", "7", "Tomatoes", "7", "Bananas", "30"]
);
