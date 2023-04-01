function shoppingList(list) {
  let products = list.shift().split("!");
  //   console.log(products);
  //   console.log(list);
  let commandParser = {
    Urgent: urgent,
    Unnecessary: unnecessary,
    Correct: correct,
    Rearrange: rearrange,
  };

  for (const line of list) {
    if (line === "Go Shopping!") {
      break;
    }

    let commandTokens = line.split(" ");
    let command = commandTokens[0];
    commandParser[command](...commandTokens.slice(1));
  }

  console.log(products.join(", "));

  function urgent(item) {
    if (!products.includes(item)) {
      products.unshift(item);
    }
  }

  function unnecessary(item) {
    if (products.includes(item)) {
      let index = products.indexOf(item);
      products.splice(index, 1);
    }
  }

  function correct(oldItem, newItem) {
    if (products.includes(oldItem)) {
      let index = products.indexOf(oldItem);
      products.splice(index, 1, newItem);
    }
  }

  function rearrange(item) {
    if (products.includes(item)) {
      let index = products.indexOf(item);
      products.splice(index, 1);
      products.push(item);
    }
  }
}

shoppingList([
  "Tomatoes!Potatoes!Bread",
  "Unnecessary Milk",
  "Urgent Tomatoes",
  "Go Shopping!",
]);
