function solve(a, b, c) {
  let largestNumber;
  if (a > b && a > c) {
    largestNumber = a;
  } else if (b > a && b > c) {
    largestNumber = b;
  } else if (c > a && c > b) {
    largestNumber = c;
  }
  console.log(`The largest number is ${largestNumber}.`);
}

function solveSwitch(a, b, c) {
  let largestNumber = Math.max(a, b, c);
  console.log(`The largest number (Mathmax) is ${largestNumber}.`);
}

solve(5, -3, 16);
solve(-3, -5, -22.5);

solveSwitch(5, -3, 16);
solveSwitch(-3, -5, -22.5);
