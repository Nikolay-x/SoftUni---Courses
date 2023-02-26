function distances(x1, y1, x2, y2) {
  function distCalculator(xf1, yf1, xf2, yf2) {
    let distance = Math.sqrt((xf2 - xf1) ** 2 + (yf2 - yf1) ** 2);
    return distance;
  }

  let distanceP1Center = distCalculator(x1, y1, 0, 0);
  let distanceP2Center = distCalculator(x2, y2, 0, 0);
  let distanceP1P2 = distCalculator(x1, y1, x2, y2);

  if (Number.isInteger(distanceP1Center)) {
    console.log(`{${x1}, ${y1}} to {0, 0} is valid`);
  } else {
    console.log(`{${x1}, ${y1}} to {0, 0} is invalid`);
  }

  if (Number.isInteger(distanceP2Center)) {
    console.log(`{${x2}, ${y2}} to {0, 0} is valid`);
  } else {
    console.log(`{${x2}, ${y2}} to {0, 0} is invalid`);
  }

  if (Number.isInteger(distanceP1P2)) {
    console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`);
  } else {
    console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`);
  }

  //   console.log(
  //     distanceP1Center.toFixed(2),
  //     distanceP2Center.toFixed(2),
  //     distanceP1P2.toFixed(2)
  //   );
}

distances(3, 0, 0, 4);
distances(2, 1, 1, 1);
distances(0, 0, 0, 0);
distances(-10, 3, 4, -50);
distances(3, 4, 5, 12);
