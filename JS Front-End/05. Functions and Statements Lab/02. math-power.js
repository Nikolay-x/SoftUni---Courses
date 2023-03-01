function toPower(num, power) {
  let result = 1;
  for (let i = 0; i < power; i++) {
    result *= num;
  }
  console.log(result);
}

toPower(2, 8);
toPower(3, 4);
