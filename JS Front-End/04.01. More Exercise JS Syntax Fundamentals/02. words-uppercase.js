function wordsUppercase(text) {
  function isLetter(character) {
    return (
      character &&
      character.length === 1 &&
      character.toLowerCase() !== character.toUpperCase()
    );
  }

  let textArr = text.split(" ");
  let result = [];
  for (const word of textArr) {
    let currentWord = "";
    for (const character of word) {
      if (isLetter(character) || !isNaN(character)) {
        currentWord += character.toUpperCase();
      } else {
        if (currentWord) {
          result.push(currentWord);
          currentWord = "";
        }
      }
    }
    if (currentWord) {
      result.push(currentWord);
    }
  }
  console.log(result.join(", "));
}

function regexWordsUpperCase(text) {
  const words = text.match(/\b\w+\b/g) || [];
  const upperCaseWords = words.map((word) => word.toUpperCase());
  console.log(upperCaseWords.join(", "));
}

wordsUppercase("Hi, how are you?");
wordsUppercase("hellow");
wordsUppercase("? kjqbfw idfkewq,fwqf   ");
wordsUppercase("? 23bfw iw3q,fwqf1   ");

regexWordsUpperCase("Hi, how are you?");
regexWordsUpperCase("hellow");
regexWordsUpperCase("? kjqbfw idfkewq,fwqf   ");
wordsUppercase("? 23bfw iw3q,fwqf1   ");
