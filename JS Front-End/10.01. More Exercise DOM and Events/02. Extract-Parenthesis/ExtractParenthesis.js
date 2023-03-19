// function extract(content) {
//   const htmlEl = document.getElementById(content);
//   let startWord = false;
//   let wordsArr = [];
//   let currentWord = "";
//   for (ch of htmlEl.textContent) {
//     if (startWord && ch !== ")") {
//       currentWord += ch;
//     }
//     if (ch === "(") {
//       startWord = true;
//     }
//     if (ch === ")") {
//       startWord = false;
//       wordsArr.push(currentWord);
//       currentWord = "";
//     }
//   }
//   let text = wordsArr.join("; ");
//   return text;
// }

function extract(content) {
  const htmlEl = document.getElementById(content);
  const pattern = /\((.*?)\)/g; // text between parentheses, including the parentheses
  const matches = htmlEl.textContent
    .match(pattern)
    .map((match) => match.substring(1, match.length - 1)); // slice away the parentheses
  let text = matches.join("; ");
  return text;
}
