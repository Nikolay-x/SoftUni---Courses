function hashtag(text) {
  let words = text.split(" ");
  let result = [];
  for (const word of words) {
    if (word.startsWith("#") && word.length > 1 && checkOnlyLetters(word)) {
      result.push(word.slice(1));
    }
  }

  console.log(result.join("\n"));

  function checkOnlyLetters(checkWord) {
    let checkWordLowercase = checkWord.toLowerCase().slice(1);
    let isValid = true;

    for (const symbol of checkWordLowercase) {
      let asciCode = symbol.charCodeAt(0);
      if (!(97 <= asciCode && asciCode <= 122)) {
        isValid = false;
        break;
      }
    }
    return isValid;
  }
}

function modernTimes(text) {
  let textArr = text.split(" ");

  for (let word of textArr) {
    if (word.startsWith("#") && word.length > 1) {
      let isValid = true;
      let wordLower = word.toLowerCase();
      for (let i = 1; i < wordLower.length; i++) {
        if (wordLower.charCodeAt(i) < 97 || wordLower.charCodeAt(i) > 122) {
          isValid = false;
          break;
        }
      }
      if (isValid) {
        console.log(word.split("#")[1]);
      }
    }
  }
}

function hashtagsDemo(text) {
  return text
    .split(" ")
    .filter((word) => word.startsWith("#") && containOnlyLetters(word))
    .map((word) => word.slice(1))
    .filter((word) => word !== "")
    .join("\n");

  function containOnlyLetters(word) {
    return [...word.toLowerCase()]
      .slice(1)
      .map((symbol) => symbol.charCodeAt(0))
      .every((charCode) => charCode >= 97 && charCode <= 122);
  }
}

hashtag("Nowadays everyone uses # to tag a #special word in #socialMedia");
hashtag(
  "The symbol # is known #variously in English-speaking #regions as the #number sign"
);

modernTimes("Nowadays everyone uses # to tag a #special word in #socialMedia");
modernTimes(
  "The symbol # is known #variously in English-speaking #regions as the #number sign"
);

hashtagsDemo("Nowadays everyone uses # to tag a #special word in #socialMedia");
hashtagsDemo(
  "The symbol # is known #variously in English-speaking #regions as the #number sign"
);
