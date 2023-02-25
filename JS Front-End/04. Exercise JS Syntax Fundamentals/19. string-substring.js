function substringDemo(word, text) {
  let textArr = text.split(" ");
  word = word.toLowerCase();
  let wordFound = false;
  for (const element of textArr) {
    elementLowerCase = element.toLowerCase();
    if (elementLowerCase === word) {
      return elementLowerCase;
    }
  }
  return `${word} not found!`;
}

function substring(word, text) {
  let textArr = text.split(" ");
  word = word.toLowerCase();
  let wordFound = false;
  for (const element of textArr) {
    elementLowerCase = element.toLowerCase();
    if (elementLowerCase === word) {
      console.log(elementLowerCase);
      wordFound = true;
      break;
    }
  }
  if (!wordFound) {
    console.log(`${word} not found!`);
  }
}

console.log(
  substringDemo("javascript", "JavaScript is the best programming language")
);
console.log(
  substringDemo("python", "JavaScript is the best programming language")
);

substring("javascript", "JavaScript is the best programming language");
substring("python", "JavaScript is the best programming language");
