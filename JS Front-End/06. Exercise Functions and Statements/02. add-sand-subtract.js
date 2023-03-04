function combineOperation(num1, num2, num3) {
  const add = (a, b) => a + b;
  const subtract = (sum, c) => sum - c;

  return subtract(add(num1, num2), num3);
}

let finalResult = (num1, num2, num3) => {
  const add = (a, b) => a + b;
  const subtract = (sum, c) => sum - c;

  return subtract(add(num1, num2), num3);
};

console.log(combineOperation(23, 6, 10));
console.log(combineOperation(1, 17, 30));
console.log(combineOperation(42, 58, 100));

console.log(finalResult(23, 6, 10));
console.log(finalResult(1, 17, 30));
console.log(finalResult(42, 58, 100));
