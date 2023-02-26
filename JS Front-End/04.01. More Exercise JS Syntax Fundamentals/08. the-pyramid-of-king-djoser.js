function pyramid(base, increment) {
  let stone = 0;
  let marble = 0;
  let lapisLazuli = 0;
  let gold = 0;
  let step = base;
  let levels = 0;
  while (step > 2) {
    levels += 1;
    stone += (step - 2) ** 2 * increment;
    if (levels % 5 === 0) {
      lapisLazuli += (step * 4 - 4) * increment;
    } else {
      marble += (step * 4 - 4) * increment;
    }
    step -= 2;
  }
  gold += step ** 2 * increment;
  let pyramidHeight = Math.floor((levels + 1) * increment);

  console.log(`Stone required: ${Math.ceil(stone)}`);
  console.log(`Marble required: ${Math.ceil(marble)}`);
  console.log(`Lapis Lazuli required: ${Math.ceil(lapisLazuli)}`);
  console.log(`Gold required: ${Math.ceil(gold)}`);
  console.log(`Final pyramid height: ${pyramidHeight}`);
}

pyramid(11, 1);
pyramid(11, 0.75);
pyramid(12, 1);
pyramid(23, 0.5);
