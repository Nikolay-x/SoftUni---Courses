function piccolo(inputArr) {
  let cars = [];
  for (let line of inputArr) {
    let [direction, carNumber] = line.split(", ");

    if (direction === "IN" && !cars.includes(carNumber)) {
      cars.push(carNumber);
    } else if (direction === "OUT" && cars.includes(carNumber)) {
      let index = cars.indexOf(carNumber);
      cars.splice(index, 1);
    }
  }

  if (cars.length === 0) {
    console.log("Parking Lot is Empty");
  } else {
    cars.sort((a, b) => a.localeCompare(b)).forEach((w) => console.log(w));
  }
}

function piccoloDemo(inputArr) {
  let cars = new Set();
  for (let line of inputArr) {
    let [direction, carNumber] = line.split(", ");

    if (direction === "IN") {
      cars.add(carNumber);
    } else if (direction === "OUT") {
      cars.delete(carNumber);
    }
  }

  if (cars.size === 0) {
    console.log("Parking Lot is Empty");
  } else {
    [...cars.keys()]
      .sort((a, b) => a.localeCompare(b))
      .forEach((w) => console.log(w));
  }
}

piccolo([
  "IN, CA2844AA",
  "IN, CA1234TA",
  "OUT, CA2844AA",
  "IN, CA9999TT",
  "IN, CA2866HI",
  "OUT, CA1234TA",
  "IN, CA2844AA",
  "OUT, CA2866HI",
  "IN, CA9876HH",
  "IN, CA2822UU",
]);

piccolo(["IN, CA2844AA", "IN, CA1234TA", "OUT, CA2844AA", "OUT, CA1234TA"]);

piccoloDemo([
  "IN, CA2844AA",
  "IN, CA1234TA",
  "OUT, CA2844AA",
  "IN, CA9999TT",
  "IN, CA2866HI",
  "OUT, CA1234TA",
  "IN, CA2844AA",
  "OUT, CA2866HI",
  "IN, CA9876HH",
  "IN, CA2822UU",
]);

piccoloDemo(["IN, CA2844AA", "IN, CA1234TA", "OUT, CA2844AA", "OUT, CA1234TA"]);
