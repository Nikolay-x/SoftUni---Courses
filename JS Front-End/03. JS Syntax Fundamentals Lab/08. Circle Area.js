function solve(radius) {
  let typeInput = typeof(radius);
  if (typeInput === 'number') {
    area = Math.pow(radius, 2) * Math.PI;
    console.log(area.toFixed(2));
  } else {
    console.log(
      `We can not calculate the circle area, because we receive a ${typeInput}.`
    );
  }
}

solve(5)
solve({5: 4, 6: 8})
solve('name')
solve([1, 3, 5])
