function printSum(start, end) {
  let array = [];
  let totalSum = 0;
  for (let i = start; i <= end; i++) {
    array.push(i);
    totalSum += i;
  }
  console.log(array.join(" "));
  console.log(`Sum: ${totalSum}`);
}

printSum(5, 10);
printSum(0, 26);
printSum(50, 60);
