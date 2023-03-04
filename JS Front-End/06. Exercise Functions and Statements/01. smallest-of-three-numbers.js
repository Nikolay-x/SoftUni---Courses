function smallestOfThreeInt(...numbers) {
  return Math.min(...numbers);
}

console.log(smallestOfThreeInt(2, 5, 3));
console.log(smallestOfThreeInt(600, 342, 123));
console.log(smallestOfThreeInt(25, 21, 4));
console.log(smallestOfThreeInt(2, -2, 2));
console.log(smallestOfThreeInt(2, -2, 2.5, 4, -8, -8.9));
