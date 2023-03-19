function solve() {
  const textInput = document.querySelector("#text");
  const namingConventionInput = document.querySelector("#naming-convention");
  const result = document.querySelector("#result");

  let words = textInput.value.toLowerCase().split(" ");
  let namingConvention = namingConventionInput.value;
  let output = ""

  if (namingConvention === "Camel Case") {
    output = toPascalCase(words);
    output = output[0].toLowerCase() + output.slice(1);
  } else if (namingConvention == "Pascal Case") {
    output = toPascalCase(words);
  } else {
    output = "Error!";
  }

  function toPascalCase(wordsFunc) {
    let output = [];
    wordsFunc.forEach((word) =>
      output.push(word.charAt(0).toUpperCase() + word.slice(1))
    );
    return output.join("");
  }

  result.textContent = output;
}
