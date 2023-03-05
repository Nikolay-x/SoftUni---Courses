function carCleanliness(commandsArr) {
  let carCleanPer = 0;
  for (const command of commandsArr) {
    if (command === "soap") {
      carCleanPer += 10;
    } else if (command === "water") {
      carCleanPer += carCleanPer * 0.2;
    } else if (command === "vacuum cleaner") {
      carCleanPer += carCleanPer * 0.25;
    } else if (command === "mud") {
      carCleanPer -= carCleanPer * 0.1;
    }
  }
  console.log(`The car is ${carCleanPer.toFixed(2)}% clean.`);
}

carCleanliness(["soap", "soap", "vacuum cleaner", "mud", "soap", "water"]);
carCleanliness([
  "soap",
  "water",
  "mud",
  "mud",
  "water",
  "mud",
  "vacuum cleaner",
]);
