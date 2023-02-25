function cookingByNumbers(numString, ...operations) {
  let num = Number(numString);
  for (let operation of operations) {
    if (operation === "chop") {
      num /= 2;
      console.log(num);
    } else if (operation === "dice") {
      num = Math.sqrt(num);
      console.log(num);
    } else if (operation === "spice") {
      num += 1;
      console.log(num);
    } else if (operation === "bake") {
      num *= 3;
      console.log(num);
    } else if (operation === "fillet") {
      num -= num * 0.2;
      console.log(num);
    }
  }
}

function cookingByNumbersEach(numString, ...operations) {
  let num = Number(numString);
  operations.forEach((operation) => {
    switch (operation) {
      case "chop":
        num /= 2;
        break;
      case "dice":
        num = Math.sqrt(num);
        break;
      case "spice":
        num++;
        break;
      case "bake":
        num *= 3;
        break;
      case "fillet":
        num -= num * 0.2;
        break;
    }

    console.log(num);
  });
}

cookingByNumbers("32", "chop", "chop", "chop", "chop", "chop");
cookingByNumbers("9", "dice", "spice", "chop", "bake", "fillet");

cookingByNumbersEach("32", "chop", "chop", "chop", "chop", "chop");
cookingByNumbersEach("9", "dice", "spice", "chop", "bake", "fillet");
