function checkMultiplication(a, b, c) {
  let result = 1;
  if (a >= 0) {
    result *= 1;
  } else {
    result *= -1;
  }
  if (b >= 0) {
    result *= 1;
  } else {
    result *= -1;
  }
  if (c >= 0) {
    result *= 1;
  } else {
    result *= -1;
  }
  if (result >= 0) {
    console.log("Positive");
  } else {
    console.log("Negative");
  }
}

function signCheck(...numbers) {
  return numbers.filter((a) => a < 0).length % 2 === 0
    ? "Positive"
    : "Negative";
}

checkMultiplication(5, 12, -15);
checkMultiplication(-6, -12, 14);
checkMultiplication(-1, -2, -3);
checkMultiplication(-5, 1, 1);

console.log(signCheck(5, 12, -15));
console.log(signCheck(-6, -12, 14));
console.log(signCheck(-1, -2, -3));
console.log(signCheck(-5, 1, 1));
