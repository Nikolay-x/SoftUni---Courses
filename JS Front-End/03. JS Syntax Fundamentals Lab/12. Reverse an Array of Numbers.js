function solve(n, array) {
  let result = [];
  for (let i = 0; i < n; i++) {
    result.push(array[i]);
  }
  result.reverse();
  let output = result.join(" ");
  console.log(output);
}

solve(3, [10, 20, 30, 40, 50]);
solve(4, [-1, 20, 99, 5]);
solve(2, [66, 43, 75, 89, 47]);
