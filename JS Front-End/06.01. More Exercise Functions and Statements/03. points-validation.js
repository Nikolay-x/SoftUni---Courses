function distances(pointsArr) {
  let x1 = pointsArr[0];
  let y1 = pointsArr[1];
  let x2 = pointsArr[2];
  let y2 = pointsArr[3];

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

  function distCalculator(xf1, yf1, xf2, yf2) {
    let distance = Math.sqrt((xf2 - xf1) ** 2 + (yf2 - yf1) ** 2);
    return distance;
  }
}

distances([3, 0, 0, 4]);
distances([2, 1, 1, 1]);
