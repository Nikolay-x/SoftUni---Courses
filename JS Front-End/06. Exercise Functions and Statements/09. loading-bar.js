function loadingBar(num) {
  let percentCount = num / 10;
  if (num === 100) {
    console.log(`${num}% Complete!`);
    console.log(`[${"%".repeat(percentCount)}]`);
  } else {
    console.log(
      `${num}% [${"%".repeat(percentCount)}${".".repeat(10 - percentCount)}]`
    );
    console.log("Still loading...");
  }
}

loadingBar(30);
loadingBar(50);
loadingBar(100);
