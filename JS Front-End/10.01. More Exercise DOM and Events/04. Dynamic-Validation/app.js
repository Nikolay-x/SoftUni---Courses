function validate() {
  const inputEmail = document.getElementById("email");

  inputEmail.addEventListener("change", changeHandler);

  function changeHandler() {
    pattern = /^[a-z]+@[a-z]+\.[a-z]+$/g;
    let output = inputEmail.value.match(pattern);
    if (!output) {
      inputEmail.classList.add("error");
    } else {
      inputEmail.classList.remove("error");
    }
  }
}
