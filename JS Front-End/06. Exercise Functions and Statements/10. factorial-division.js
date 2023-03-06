function factorialDivision(num1, num2) {
  let num1Factorial = 1;
  let num2Factorial = 1;
  for (let i = num1; i >= 1; i--) {
    num1Factorial *= i;
  }
  for (let i = num2; i >= 1; i--) {
    num2Factorial *= i;
  }

  console.log((num1Factorial / num2Factorial).toFixed(2));
}

function factorialDivisionRecursion(num1, num2) {
  let num1Factorial = factorial(num1);
  let num2Factorial = factorial(num2);

  function factorial(n) {
    if (n === 1) {
      return n;
    }
    return n * factorial(n - 1);
  }

  console.log((num1Factorial / num2Factorial).toFixed(2));
}

function factorialDivisionMath(num1, num2) {
  let result = 1;
  if (num1 >= num2) {
    for (let i = num1; i > num2; i--) {
      result *= i;
    }
  } else {
    for (let i = num1; i < num2; i++) {
      result *= i;
    }
    result = 1 / result;
  }
  console.log(result.toFixed(2));
}

factorialDivision(5, 2);
factorialDivision(6, 2);
factorialDivision(7, 3);

factorialDivisionRecursion(5, 2);
factorialDivisionRecursion(6, 2);
factorialDivisionRecursion(7, 3);

factorialDivisionMath(5, 2);
factorialDivisionMath(6, 2);
factorialDivisionMath(7, 3);

factorialDivision(1, 12);
factorialDivision(10, 12);
factorialDivision(12, 13);

factorialDivisionMath(1, 12);
factorialDivisionMath(10, 12);
factorialDivisionMath(12, 13);
