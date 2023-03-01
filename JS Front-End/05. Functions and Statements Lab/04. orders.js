function ordersSum(product, qty) {
  let price;
  switch (product) {
    case "coffee":
      price = 1.5;
      break;
    case "water":
      price = 1;
      break;
    case "coke":
      price = 1.4;
      break;
    case "snacks":
      price = 2;
      break;
    default:
      price = 0;
      break;
  }
  let result = price * qty;
  console.log(result.toFixed(2));
}

ordersSum("water", 5);
ordersSum("coffee", 2);
