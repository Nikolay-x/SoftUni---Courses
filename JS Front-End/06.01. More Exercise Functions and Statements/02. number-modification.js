function numberDigitsGTFive(num) {
  while (isNumberDigitsAvgGTFive(num) < 5) {
    num *= 10;
    num += 9;
  }

  function isNumberDigitsAvgGTFive(num) {
    let numDigitsArr = num
      .toString()
      .split("")
      .map((digitStr) => Number(digitStr));
    return numDigitsArr.reduce((a, b) => a + b, 0) / numDigitsArr.length;
  }

  console.log(num);
}

numberDigitsGTFive(101);
numberDigitsGTFive(5835);
