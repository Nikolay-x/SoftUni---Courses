function digitsSum(num) {
  //   let stringNum = String(num);
  let stringNum = num.toString();
  let totalSum = 0;
  for (let el of stringNum) {
    digit = Number(el);
    totalSum += digit;
  }
  console.log(totalSum);
}

function digitsSumMath(num) {
  let totalSum = 0;
  while (num > 0) {
    let digit = num % 10;
    totalSum += digit;
    // num -= digit;
    // num /= 10;
    num = Math.floor(num / 10);
  }
  console.log(totalSum);
}

digitsSum(245678);
digitsSum(97561);
digitsSum(543);

digitsSumMath(245678);
digitsSumMath(97561);
digitsSumMath(543);
