function attachEvents() {
  const phonebookContainer = document.getElementById("phonebook");
  const loadBtn = document.getElementById("btnLoad");
  const personInput = document.getElementById("person");
  const phoneInput = document.getElementById("phone");
  const createBtn = document.getElementById("btnCreate");
  const BASE_URL = "http://localhost:3030/jsonstore/phonebook/";

  loadBtn.addEventListener("click", loadPhoneBookHandler);
  createBtn.addEventListener("click", createPhoneBookHandler);

  async function loadPhoneBookHandler() {
    try {
      const phoneBookResponse = await fetch(`${BASE_URL}`);
      let phonebookData = await phoneBookResponse.json();
      phonebookContainer.innerHTML = "";
      // console.log(phonebookData);

      phonebookData = Object.values(phonebookData);
      for (const { phone, person, _id } of phonebookData) {
        const li = document.createElement("li");
        const button = document.createElement("button");

        li.textContent = `${person}: ${phone}`;
        button.textContent = "Delete";
        button.id = _id;
        button.addEventListener("click", deletePhoneBookHandler);
        li.appendChild(button);
        phonebookContainer.appendChild(li);
      }
    } catch (err) {
      console.error(err);
    }
  }

  function createPhoneBookHandler() {
    const person = personInput.value;
    const phone = phoneInput.value;
    const httpHeaders = {
      method: "POST",
      body: JSON.stringify({ person, phone }),
    };

    fetch(BASE_URL, httpHeaders)
      .then((res) => res.json())
      .then(() => {
        loadPhoneBookHandler();
        personInput.value = "";
        phoneInput.value = "";
      })
      .catch((err) => {
        console.error(err);
      });
  }

  async function deletePhoneBookHandler(e) {
    const id = e.currentTarget.id;
    // const id = this.id;
    // console.log(id);
    const httpHeaders = {
      method: "DELETE",
    };

    fetch(`${BASE_URL}${id}`, httpHeaders)
      .then((res) => res.json())
      .then(loadPhoneBookHandler)
      .catch((err) => {
        console.error(err);
      });
  }
}

attachEvents();
