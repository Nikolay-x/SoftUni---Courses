function calculator(num1, num2, operator) {
  let multiply = (a, b) => a * b;
  let divide = (a, b) => a / b;
  let add = (a, b) => a + b;
  let subtract = (a, b) => a - b;

  let result;
  switch (operator) {
    case "multiply":
      result = multiply(num1, num2);
      break;
    case "divide":
      result = divide(num1, num2);
      break;
    case "add":
      result = add(num1, num2);
      break;
    case "subtract":
      result = subtract(num1, num2);
      break;
  }

  console.log(result);
}

function calculatorArrow(num1, num2, operator) {
  let result = {
    multiply: num1 * num2,
    divide: num1 / num2,
    add: num1 + num2,
    subtract: num1 - num2,
  };
  console.log(`${result[operator]}`);
}

calculator(5, 5, "multiply");
calculator(40, 8, "divide");
calculator(61, 2, "divide");
calculator(12, 19, "add");
calculator(50, 13, "subtract");

calculatorArrow(5, 5, "multiply");
calculatorArrow(40, 8, "divide");
calculatorArrow(61, 2, "divide");
calculatorArrow(12, 19, "add");
calculatorArrow(50, 13, "subtract");
