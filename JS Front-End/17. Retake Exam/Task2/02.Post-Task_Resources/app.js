window.addEventListener("load", solve);

function solve() {
  let currentTasks = [];
  let taskToEdit = {};

  const inputDOMSelectors = {
    title: document.getElementById("task-title"),
    category: document.getElementById("task-category"),
    content: document.getElementById("task-content"),
  };

  const otherDOMSelectors = {
    publishBtn: document.getElementById("publish-btn"),
    reviewTasks: document.getElementById("review-list"),
    publishedTasks: document.getElementById("published-list"),
  };

  otherDOMSelectors.publishBtn.addEventListener("click", publishTaskHandler);

  function publishTaskHandler(event) {
    if (event) {
      event.preventDefault();
    }

    let allInputsAreNonEmpty = Object.values(inputDOMSelectors).every(
      (input) => input.value.trim() !== ""
    );

    if (!allInputsAreNonEmpty) {
      return;
    }

    const { title, category, content } = inputDOMSelectors;

    currentTasks.push({
      title: title.value,
      category: category.value,
      content: content.value,
    });

    const li = createElement("li", otherDOMSelectors.reviewTasks, "", [
      "rpost",
    ]);
    // li.title = title;
    const article = createElement("article", li);
    createElement("h4", article, `${title.value}`);
    createElement("p", article, `Category: ${category.value}`);
    createElement("p", article, `Content: ${content.value}`);
    const editBtn = createElement("button", li, "Edit", ["action-btn", "edit"]);
    const postBtn = createElement("button", li, "Post", ["action-btn", "post"]);

    editBtn.addEventListener("click", editHandler);
    postBtn.addEventListener("click", postHandler);

    clearAllInputs();
  }

  function editHandler() {
    let li = this.parentNode;
    let h4 = li.querySelector("article > h4");
    let title = h4.textContent;
    // console.log(id);
    taskToEdit = currentTasks.find((t) => t.title === title);
    // console.log(currentTasks);
    // console.log(taskToEdit);

    for (const key in inputDOMSelectors) {
      inputDOMSelectors[key].value = taskToEdit[key];
    }

    this.parentNode.remove();
  }

  function postHandler() {
    const taskRef = this.parentNode;

    const editBtn = taskRef.querySelector(".edit");
    const postBtn = taskRef.querySelector(".post");

    otherDOMSelectors.publishedTasks.appendChild(taskRef);

    editBtn.remove();
    postBtn.remove();
  }

  function clearAllInputs() {
    Object.values(inputDOMSelectors).forEach((input) => {
      input.value = "";
    });
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
