function solve(string, startIndex, count) {
  let endIndex = startIndex + count;
  let result = string.substring(startIndex, endIndex);
  console.log(result);
}

solve("ASentence", 1, 8);
solve("SkipWord", 4, 7);
