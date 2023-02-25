function pascalSplitter(text) {
  let currentWord = "";
  let upperCase = "";
  let result = [];
  for (let i = 0; i < text.length; i++) {
    upperCase = text[i].toUpperCase();
    if (text[i] === upperCase) {
      if (currentWord.length > 0) {
        result.push(currentWord);
      }
      currentWord = "";
      currentWord += text[i];
      if (i === text.length - 1) {
        result.push(currentWord);
      }
    } else {
      currentWord += text[i];
      if (i === text.length - 1) {
        result.push(currentWord);
      }
    }
  }
  console.log(result.join(", "));
}

function pascalCaseSplit(text) {
  let pattern = "[A-Z][a-z]*";
  let matches = text.matchAll(pattern);
  let arr = [];

  for (let word of matches) {
    arr.push(word[0]);
  }

  console.log(arr.join(", "));
}

function pascalCaseSpliter(text) {
  let output = "";
  for (const symbol of text) {
    const asciCode = symbol.charCodeAt(0);
    if (65 <= asciCode && asciCode <= 90) {
      if (output.length > 0) {
        output += ", ";
      }
      output += symbol;
    } else {
      output += symbol;
    }
  }
  console.log(output);
}

pascalSplitter("SplitMeIfYouCanHaHaYouCantOrYouCan");
pascalSplitter("HoldTheDoor");
pascalSplitter("ThisIsSoAnnoyingToDo");
pascalSplitter("ThisIsS");

pascalCaseSplit("SplitMeIfYouCanHaHaYouCantOrYouCan");
pascalCaseSplit("HoldTheDoor");
pascalCaseSplit("ThisIsSoAnnoyingToDo");

pascalCaseSpliter("SplitMeIfYouCanHaHaYouCantOrYouCan");
pascalCaseSpliter("HoldTheDoor");
pascalCaseSpliter("ThisIsSoAnnoyingToDo");
