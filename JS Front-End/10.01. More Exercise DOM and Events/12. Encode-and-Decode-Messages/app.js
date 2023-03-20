function encodeAndDecodeMessages() {
  const [btnEncode, btnDecode] = Array.from(
    document.querySelectorAll("button")
  );
  const [sendText, receivedText] = Array.from(
    document.querySelectorAll("textarea")
  );

  btnEncode.addEventListener("click", (x) => {
    let output = "";
    for (const letter of sendText.value) {
      output += String.fromCharCode(letter.charCodeAt(0) + 1);
    }
    sendText.value = "";
    receivedText.value = output;
  });

  btnDecode.addEventListener("click", (x) => {
    let output = "";
    for (const letter of receivedText.value) {
      output += String.fromCharCode(letter.charCodeAt(0) - 1);
    }
    receivedText.value = output;
  });
}
