function oddEvenSums(num) {
  let numDigits = num
    .toString()
    .split("")
    .map((numString) => Number(numString));
  let evenSum = 0;
  let oddSum = 0;
  for (const digit of numDigits) {
    if (digit % 2 === 0) {
      evenSum += digit;
    } else {
      oddSum += digit;
    }
  }
  console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
}

oddEvenSums(1000435);
oddEvenSums(3495892137259234);
