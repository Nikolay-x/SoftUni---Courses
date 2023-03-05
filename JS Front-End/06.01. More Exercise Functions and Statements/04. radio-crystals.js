function radioCrystals(crystalArr) {
  let desiredThickness = crystalArr.shift();

  let cut = (thickness) => thickness / 4;
  let lap = (thickness) => thickness - thickness * 0.2;
  let grind = (thickness) => thickness - 20;
  let etch = (thickness) => thickness - 2;
  let xRay = (thickness) => thickness + 1;
  let transportAndWash = (thickness) => Math.floor(thickness);

  for (let i = 0; i < crystalArr.length; i++) {
    let currentChunk = crystalArr[i];

    let cutCount = 0;
    let lapCount = 0;
    let grindCount = 0;
    let etchCount = 0;

    console.log(`Processing chunk ${currentChunk} microns`);

    while (currentChunk !== desiredThickness) {
      while (currentChunk / 4 >= desiredThickness) {
        currentChunk = cut(currentChunk);
        cutCount += 1;
      }
      if (cutCount > 0) {
        console.log(`Cut x${cutCount}`);
        console.log(`Transporting and washing`);
        currentChunk = transportAndWash(currentChunk);
      }

      while (currentChunk - currentChunk * 0.2 >= desiredThickness) {
        currentChunk = lap(currentChunk);
        lapCount += 1;
      }
      if (lapCount > 0) {
        console.log(`Lap x${lapCount}`);
        console.log(`Transporting and washing`);
        currentChunk = transportAndWash(currentChunk);
      }

      while (currentChunk - 20 >= desiredThickness) {
        currentChunk = grind(currentChunk);
        grindCount += 1;
      }
      if (grindCount > 0) {
        console.log(`Grind x${grindCount}`);
        console.log(`Transporting and washing`);
        currentChunk = transportAndWash(currentChunk);
      }

      while (currentChunk - 2 >= desiredThickness - 1) {
        currentChunk = etch(currentChunk);
        etchCount += 1;
      }
      if (etchCount > 0) {
        console.log(`Etch x${etchCount}`);
        console.log(`Transporting and washing`);
        currentChunk = transportAndWash(currentChunk);
      }

      if (currentChunk < desiredThickness) {
        currentChunk = xRay(currentChunk);
        console.log(`X-ray x1`);
      }
    }
    console.log(`Finished crystal ${desiredThickness} microns`);
  }
}

radioCrystals([1375, 50000]);
radioCrystals([1000, 4000, 8100]);
