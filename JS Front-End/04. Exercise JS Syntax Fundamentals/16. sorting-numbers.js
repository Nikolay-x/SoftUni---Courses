function sortingNumbers(numbers) {
  numbers.sort((a, b) => {
    let result = a - b;
    return result;
  });

  let minNumbers = [];
  let maxNumbers = [];
  for (let i = 0; i < Math.ceil(numbers.length / 2); i++) {
    minNumbers.push(numbers[i]);
  }
  for (let i = Math.ceil(numbers.length / 2); i < numbers.length; i++) {
    maxNumbers.push(numbers[i]);
  }
  maxNumbers.reverse();

  let result = [];
  for (let i = 0; i < maxNumbers.length; i++) {
    result.push(minNumbers[i]);
    result.push(maxNumbers[i]);
  }
  if (minNumbers.length > maxNumbers.length) {
    result.push(minNumbers[minNumbers.length - 1]);
  }

  //   console.log(numbers);
  //   console.log(minNumbers);
  //   console.log(maxNumbers);
  return result;
}

function solve(numbers) {
  numbers.sort((a, b) => a - b);
  let sortedNumbers = [];

  while (numbers.length !== 0) {
    sortedNumbers.push(numbers.shift());
    sortedNumbers.push(numbers.pop());
  }

  return sortedNumbers.filter((number) => typeof number !== "undefined");
}

function solveDemo(numbers) {
  let sorted = [...numbers].sort((a, b) => a - b);
  let step = 0;
  let result = [];
  while (sorted.length > 0) {
    if (step % 2 === 0) {
      let firstEl = sorted.shift();
      result.push(firstEl);
    } else {
      let lastEl = sorted.pop();
      result.push(lastEl);
    }
    step++;
  }
  return result;
}

console.log(sortingNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));
console.log(sortingNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56, 60]));

console.log(solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));
console.log(solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56, 60]));

console.log(solveDemo([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));
console.log(solveDemo([1, 65, 3, 52, 48, 63, 31, -3, 18, 56, 60]));
