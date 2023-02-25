function sameNumbers(num) {
  let totalSum = 0;
  let count = 0;
  while (num > 0) {
    digit = num % 10;
    totalSum += digit;
    count += 1;
    num = Math.floor(num / 10);
  }
  if (totalSum === 0) {
    console.log("true");
  } else {
    if (totalSum / count === digit) {
      console.log("true");
    } else {
      console.log("false");
    }
  }
  console.log(totalSum);
}

function solve(num) {
  let arr = Array.from(num.toString());
  let templateDigit = arr[0];
  let areDigitsSame = true;
  let totalSum = 0;
  for (digit of arr) {
    if (digit !== templateDigit) {
      areDigitsSame = false;
    }
    totalSum += Number(digit);
  }
  console.log(areDigitsSame);
  console.log(totalSum);
}

sameNumbers(2222222);
sameNumbers(1234);
sameNumbers(0);

solve(2222222);
solve(1234);
solve(0);
