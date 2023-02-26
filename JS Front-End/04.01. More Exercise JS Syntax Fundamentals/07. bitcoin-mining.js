function mining(arr) {
  let totalAmnt = 0;
  let count = 0;
  let firstBitcoinDay = 0;
  for (let i = 0; i < arr.length; i++) {
    if ((i + 1) % 3 === 0) {
      totalAmnt += 0.7 * arr[i] * 67.51;
    } else {
      totalAmnt += arr[i] * 67.51;
    }
    if (totalAmnt >= 11949.16 && count === 0) {
      firstBitcoinDay = i + 1;
      count += 1;
    }
  }

  let bitcoins = Math.floor(totalAmnt / 11949.16);
  if (bitcoins) {
    totalAmnt -= bitcoins * 11949.16;
  }

  console.log(`Bought bitcoins: ${bitcoins}`);
  if (bitcoins) {
    console.log(`Day of the first purchased bitcoin: ${firstBitcoinDay}`);
  }
  console.log(`Left money: ${totalAmnt.toFixed(2)} lv.`);
}

mining([100, 200, 300]);
mining([50, 100]);
mining([3124.15, 504.212, 2511.124]);
