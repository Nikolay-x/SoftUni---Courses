function spiceMine(startingYield) {
  let yield = startingYield;
  let days = 0;
  let totalAmnt = 0;
  while (yield >= 100) {
    totalAmnt += yield;
    yield -= 10;
    days += 1;
    totalAmnt -= 26;
  }

  if (totalAmnt >= 26) {
    totalAmnt -= 26;
  } else {
    totalAmnt = 0;
  }

  console.log(days);
  console.log(totalAmnt);
}

spiceMine(111);
spiceMine(450);
