function palindrome(numArr) {
  for (const num of numArr) {
    let numStr = num.toString();
    console.log(numStr.split("").reverse().join("") === numStr);
  }
}

palindrome([123, 323, 421, 121]);
palindrome([32, 2, 232, 1010]);
