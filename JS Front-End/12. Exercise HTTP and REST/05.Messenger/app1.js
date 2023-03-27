function attachEvents() {
  const textarea = document.querySelector("#messages");
  const nameInput = document.querySelector(
    "#controls > div:nth-child(1) > input[type=text]"
  );
  const messageInput = document.querySelector(
    "#controls > div:nth-child(2) > input[type=text]"
  );
  const sendBtn = document.getElementById("submit");
  const refreshBtn = document.getElementById("refresh");
  const BASE_URL = "http://localhost:3030/jsonstore/messenger";

  sendBtn.addEventListener("click", postHandler);
  refreshBtn.addEventListener("click", refreshHandler);

  async function postHandler() {
    const author = nameInput.value;
    const content = messageInput.value;
    const httpHeaders = {
      method: "POST",
      body: JSON.stringify({ author, content }),
    };
    const messageToPost = await fetch(BASE_URL, httpHeaders);
    nameInput.value = "";
    messageInput.value = "";
  }

  async function refreshHandler() {
    const messagesRes = await fetch(BASE_URL);
    const messagesData = await messagesRes.json();
    textarea.textContent = "";
    let output = [];
    // console.log(messagesData);
    for (let key in messagesData) {
      let { author, content } = messagesData[key];
      //   console.log(author);
      //   console.log(content);
      output.push(`${author}: ${content}`);
      textarea.textContent = output.join("\n");
    }
  }
}

attachEvents();
