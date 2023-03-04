let text =
  "Password must be between 6 and 10 characters. Password must consist only of letters and digits. Password must have at least 2 digits";

let regex = /\d+/g;

// regex exec
let execution = regex.exec(text);
let value = execution[0];
let index = execution.index;
let input = execution.input;
console.log(execution);
console.log(value);
console.log(index);
console.log(input);
let execution1 = regex.exec(text);
let value1 = execution1[0];
console.log(value1);
let execution2 = regex.exec(text);
let value2 = execution2[0];
console.log(value2);

// regex while
// let execution = regex.exec(text);
// while (execution !== null) {
//   let value = execution[0];
//   console.log(value);
//   execution = regex.exec(text);
// }

// regex matchAll
// console.log([...text.matchAll(regex)][0]);

// regex test
// console.log(regex.test(text));

// regex interpolation
// let regexInterpolation = new RegExp(`${text}, 'g`);
// console.log(regexInterpolation.test);
