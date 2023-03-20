function solve() {
  const possibleAnswers = Array.from(document.querySelectorAll(".answer-text"));
  const sections = document.querySelectorAll("section");
  const resultsBox = document.querySelector("#results");
  const resultsLine = document.querySelector("#results h1");

  let correctAnswers = [
    "onclick",
    "JSON.stringify()",
    "A programming API for HTML and XML documents",
  ];
  let correctAnswersNum = 0;
  let index = 0;

  possibleAnswers.map((a) =>
    a.addEventListener("click", (e) => {
      if (correctAnswers.includes(e.target.textContent)) {
        correctAnswersNum += 1;
      }

      let currentSection = sections[index];
      currentSection.style.display = "none";

      if (sections[index + 1] !== undefined) {
        let nextSection = sections[index + 1];
        nextSection.style.display = "block";
        index += 1;
      } else {
        resultsBox.style.display = "block";
        if (correctAnswersNum !== 3) {
          resultsLine.textContent = `You have ${correctAnswersNum} right answers`;
        } else {
          resultsLine.textContent = "You are recognized as top JavaScript fan!";
        }
      }
    })
  );
}
