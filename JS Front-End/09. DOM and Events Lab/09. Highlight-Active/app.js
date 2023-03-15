function focused() {
  const focusedInputs = document.querySelectorAll('input[type="text"]');
  for (const focusedInput of focusedInputs) {
    focusedInput.addEventListener("focus", function () {
      focusedInput.parentElement.classList.add("focused");
    });
    focusedInput.addEventListener("blur", function () {
      focusedInput.parentElement.classList.remove("focused");
    });
  }
}

// function focused() {
//   const inputs = document.querySelectorAll("input[type='text']");
//   for (let i = 0; i < inputs.length; i++) {
//     const input = inputs[i];
//     input.addEventListener("focus", (event) => {
//       const div = event.currentTarget.parentNode;
//       div.classList.add("focused");
//     });
//     input.addEventListener("blur", (event) => {
//       const div = event.currentTarget.parentNode;
//       div.classList.remove("focused");
//     });
//   }
// }
