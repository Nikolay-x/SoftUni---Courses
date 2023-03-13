function garage(list) {
  let cars = {};
  for (const line of list) {
    let [garage, carTokens] = line.split(" - ");
    if (!cars.hasOwnProperty(garage)) {
      cars[garage] = [];
    }
    cars[garage].push(carTokens);
  }

  for (const garage of Object.entries(cars)) {
    console.log(`Garage № ${garage[0]}`);

    for (const car of garage[1]) {
      let properties = car.split(", ");
      let propertiesList = [];

      for (const property of properties) {
        let [key, value] = property.split(": ");
        propertiesList.push(`${key} - ${value}`);
      }

      console.log(`--- ${propertiesList.join(", ")}`);
    }
  }
}

garage([
  "1 - color: blue, fuel type: diesel",
  "1 - color: red, manufacture: Audi",
  "2 - fuel type: petrol",
  "4 - color: dark blue, fuel type: diesel, manufacture: Fiat",
]);
