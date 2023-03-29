window.addEventListener("load", solve);

// For judge always use Array.from() to transform a collection -> querySelectorAll, children
function solve() {
  const storyState = {
    firstName: null,
    lastName: null,
    age: null,
    title: null,
    genre: null,
    story: null,
  };

  const inputDOMSelectors = {
    firstName: document.getElementById("first-name"),
    lastName: document.getElementById("last-name"),
    age: document.getElementById("age"),
    title: document.getElementById("story-title"),
    genre: document.getElementById("genre"),
    story: document.getElementById("story"),
  };

  const otherDOMSelectors = {
    publishBtn: document.getElementById("form-btn"),
    previewList: document.getElementById("preview-list"),
    mainContainer: document.getElementById("main"),
  };

  otherDOMSelectors.publishBtn.addEventListener("click", publishStoryHandler);

  function publishStoryHandler() {
    // debugger;
    // console.log(Object.values(inputDOMSelectors));
    const allFieldsHaveValue = Object.values(inputDOMSelectors).every(
      (input) => input.value !== ""
    );
    // console.log(allFieldsHaveValue);

    if (!allFieldsHaveValue) {
      // console.log("Empty field");
      return;
    }

    const { firstName, lastName, age, title, genre, story } = inputDOMSelectors;
    const li = createElement("li", otherDOMSelectors.previewList, null, [
      "story-info",
    ]);
    const article = createElement("article", li);
    createElement("h4", article, `Name: ${firstName.value} ${lastName.value}`);
    createElement("p", article, `Age: ${age.value}`);
    createElement("p", article, `Title: ${title.value}`);
    createElement("p", article, `Genre: ${genre.value}`);
    createElement("p", article, story.value);
    const saveBtn = createElement("button", li, "Save Story", ["save-btn"]);
    const editBtn = createElement("button", li, "Edit Story", ["edit-btn"]);
    const deleteBtn = createElement("button", li, "Delete Story", [
      "delete-btn",
    ]);

    editBtn.addEventListener("click", editStoryHandler);
    deleteBtn.addEventListener("click", deleteStoryHandler);
    saveBtn.addEventListener("click", saveStoryHandler);

    for (const key in inputDOMSelectors) {
      storyState[key] = inputDOMSelectors[key].value;
    }

    clearAllInputs();
    otherDOMSelectors.publishBtn.setAttribute("disabled", true);
  }

  function editStoryHandler() {
    // console.log(storyState);
    // console.log(Object.values(inputDOMSelectors).map((input) => input.value));
    for (const key in inputDOMSelectors) {
      inputDOMSelectors[key].value = storyState[key];
    }

    otherDOMSelectors.publishBtn.removeAttribute("disabled");
    otherDOMSelectors.previewList.innerHTML = "";
    createElement("h3", otherDOMSelectors.previewList, "Preview");
  }

  function deleteStoryHandler(event) {
    const liItem = event.currentTarget.parentNode;
    // const liItem = this.parentNode;
    liItem.remove();
    otherDOMSelectors.publishBtn.removeAttribute("disabled");
  }

  function saveStoryHandler() {
    otherDOMSelectors.mainContainer.innerHTML = "";
    createElement(
      "h1",
      otherDOMSelectors.mainContainer,
      "Your scary story is saved!"
    );
  }

  function clearAllInputs() {
    Object.values(inputDOMSelectors).forEach((input) => (input.value = ""));
  }

  // Notes and Tests
  // const p = createElement(
  //   "p",
  //   document.getElementById("preview-list"),
  //   "My paragraph",
  //   ["story"],
  //   "my-id",
  //   null
  // );

  // const img = createElement(
  //   "img",
  //   document.getElementById("preview-list"),
  //   null,
  //   ["story"],
  //   "my-img-id",
  //   {
  //     src: "https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_1920,f_auto/A-Alamy-BXWK5E_vvmkuf.jpg",
  //   }
  // );

  // type = string
  // content = string (text content)
  // id = string
  // classes = array of strings
  // attributes = object
  // useInnerHtml = boolean
  function createElement(
    type,
    parentNode,
    content,
    classes,
    id,
    attributes,
    useInnerHtml
  ) {
    const htmlElement = document.createElement(type);

    if (content && useInnerHtml) {
      htmlElement.innerHTML = content;
    } else {
      if (content && type !== "input" && type !== "textarea") {
        htmlElement.textContent = content;
      }

      if (content && type === "input") {
        htmlElement.value = content;
      }

      if (content && type === "textarea") {
        htmlElement.value = content;
      }
    }

    if (classes && classes.length > 0) {
      htmlElement.classList.add(...classes);
    }

    if (id) {
      htmlElement.id = id;
    }

    // { src: "link", href: "link" }
    if (attributes) {
      for (const key in attributes) {
        htmlElement.setAttribute(key, attributes[key]);
        // htmlElement[key] = attributes[key];
      }
    }

    if (parentNode) {
      parentNode.appendChild(htmlElement);
    }

    return htmlElement;
  }
}
