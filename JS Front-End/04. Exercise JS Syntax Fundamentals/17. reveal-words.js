function revealWords(wordsStr, text) {
  let words = wordsStr.split(", ");
  let textArr = text.split(" ");

  for (let word of words) {
    for (let el of textArr) {
      if (el.includes("*") && el.length == word.length) {
        text = text.replace(el, word);
      }
    }
  }
  console.log(text);
}

revealWords(
  "great",
  "softuni is ***** place for learning new programming languages"
);
revealWords(
  "great, learning",
  "softuni is ***** place for ******** new programming languages"
);
