function sequence(inputArr) {
  let numsArr = [];
  for (const line of inputArr) {
    numsArr.push(JSON.parse(line).sort((a, b) => b - a));
  }

  let result = [];
  while (numsArr.length > 0) {
    let currentArr = numsArr.shift();
    let flag = true;
    for (let i = 0; i < numsArr.length; i++) {
      if (arraysAreEqual(currentArr, numsArr[i])) {
        flag = false;
        break;
      }
    }
    if (flag) {
      result.push(currentArr);
    }
  }

  result.sort((a, b) => a.length - b.length);
  result.forEach((a) => console.log(`[${a.join(", ")}]`));

  function arraysAreEqual(array1, array2) {
    if (array1.length !== array2.length) {
      return false;
    }
    for (let i = 0; i < array1.length; i++) {
      if (array1[i] !== array2[i]) {
        return false;
      }
    }
    return true;
  }
}

sequence([
  "[-3, -2, -1, 0, 1, 2, 3, 4]",
  "[10, 1, -17, 0, 2, 13]",
  "[4, -3, 3, -2, 2, -1, 1, 0]",
]);

sequence([
  "[7.14, 7.180, 7.339, 80.099]",
  "[7.339, 80.0990, 7.140000, 7.18]",
  "[7.339, 7.180, 7.14, 80.099]",
]);
