function repeatString(str, repeat) {
  output = "";
  for (let i = 0; i < repeat; i++) {
    output += str;
  }
  return output;
}

console.log(repeatString("abc", 3));
console.log(repeatString("String", 2));
