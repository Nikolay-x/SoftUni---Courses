function oddOccurrences(inputStr) {
  let words = {};
  let wordsLower = inputStr.toLowerCase().split(" ");
  for (let word of wordsLower) {
    if (words.hasOwnProperty(word)) {
      words[word] += 1;
    } else {
      words[word] = 1;
    }
  }

  let oddWords = [];
  Object.entries(words)
    .filter((w) => w[1] % 2 !== 0)
    .forEach((w) => {
      oddWords.push(w[0]);
    });
  console.log(oddWords.join(" "));
}

oddOccurrences("Java C# Php PHP Java PhP 3 C# 3 1 5 C#");
oddOccurrences("Cake IS SWEET is Soft CAKE sweet Food");
