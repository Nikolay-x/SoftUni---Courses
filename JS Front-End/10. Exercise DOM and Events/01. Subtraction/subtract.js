function subtract() {
  const numOne = Number(document.getElementById("firstNumber").value);
  const numTwo = parseFloat(document.querySelector("#secondNumber").value);
  document.querySelector("#result").textContent = numOne - numTwo;
}
