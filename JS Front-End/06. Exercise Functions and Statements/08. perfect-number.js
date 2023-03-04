function numAliquotSum(num) {
  let divisorsSum = 0;
  for (let i = 1; i <= num / 2; i++) {
    if (num % i === 0) {
      divisorsSum += i;
    }
  }
  if (num === divisorsSum) {
    console.log("We have a perfect number!");
  } else {
    console.log("It's not so perfect.");
  }
}

function numAliquotSumDemo(num) {
  let divisors = [];
  for (let i = 1; i <= num / 2; i++) {
    if (num % i === 0) {
      divisors.push(i);
    }
  }

  let divisorsSum = divisors.reduce(
    (previuosVal, currentVal) => previuosVal + currentVal,
    0
  );

  if (num === divisorsSum) {
    console.log("We have a perfect number!");
  } else {
    console.log("It's not so perfect.");
  }
}

numAliquotSum(6);
numAliquotSum(28);
numAliquotSum(1236498);

numAliquotSumDemo(6);
numAliquotSumDemo(28);
numAliquotSumDemo(1236498);
