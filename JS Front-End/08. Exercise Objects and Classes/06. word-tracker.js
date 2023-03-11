function wordTracker(inputArr) {
  let searchWords = inputArr.shift().split(" ");
  let words = [];
  for (let word of searchWords) {
    // let count = 0;
    // for (let w of inputArr) {
    //   if (w === word) {
    //     count += 1;
    //   }

    let count = inputArr.filter((w) => w === word).length;

    words.push({ word, count });
  }

  words
    .sort((w1, w2) => w2.count - w1.count)
    .forEach((w) => {
      console.log(`${w.word} - ${w.count}`);
    });
}

wordTracker([
  "this sentence",
  "In",
  "this",
  "sentence",
  "you",
  "have",
  "to",
  "count",
  "the",
  "occurrences",
  "of",
  "the",
  "words",
  "this",
  "and",
  "sentence",
  "because",
  "this",
  "is",
  "your",
  "task",
]);

wordTracker([
  "is the",
  "first",
  "sentence",
  "Here",
  "is",
  "another",
  "the",
  "And",
  "finally",
  "the",
  "the",
  "sentence",
]);
