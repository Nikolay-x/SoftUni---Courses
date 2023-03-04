function nxnMatrix(num) {
  let row = [];
  let matrix = [];
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      row.push(num);
    }
    matrix.push(row.join(" "));
    row = [];
  }
  console.log(matrix.join("\n"));
}

let matrix = (n) =>
  new Array(n)
    .fill(new Array(n).fill(n))
    .forEach((row) => console.log(row.join(" ")));

nxnMatrix(3);
nxnMatrix(7);
nxnMatrix(2);

matrix(3);
matrix(7);
matrix(2);
