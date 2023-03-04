function validPassword(password) {
  let lengthIsValid = (password) =>
    6 <= password.length && password.length <= 10;
  let lettersDigitsOnly = (password) => /^[A-Za-z0-9]+$/gm.test(password);
  let atLeastTwoDigits = (password) =>
    [...password.matchAll(/[0-9]/gm)].length >= 2;
  passIsValid = true;

  if (!lengthIsValid(password)) {
    console.log("Password must be between 6 and 10 characters");
    passIsValid = false;
  }

  if (!lettersDigitsOnly(password)) {
    console.log("Password must consist only of letters and digits");
    passIsValid = false;
  }

  if (!atLeastTwoDigits(password)) {
    console.log("Password must have at least 2 digits");
    passIsValid = false;
  }

  if (passIsValid) {
    console.log("Password is valid");
  }
}

validPassword("logIn");
validPassword("MyPass123");
validPassword("Pa$s$s");
