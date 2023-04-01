window.addEventListener("load", solve);

function solve() {
  let totalLikes = 0;
  const inputDOMSelectors = {
    genre: document.querySelector("input[name = 'genre']"),
    name: document.querySelector("input[name = 'name']"),
    author: document.querySelector("input[name = 'author']"),
    date: document.querySelector("input[name = 'date']"),
  };

  const otherDOMSelectors = {
    addBtn: document.getElementById("add-btn"),
    allHitsContainer: document.querySelector(".all-hits-container"),
    savedContainer: document.querySelector(".saved-container"),
    totalLikesContainer: document.querySelector(".likes > p"),
  };

  otherDOMSelectors.addBtn.addEventListener("click", addSongHandler);

  function addSongHandler(event) {
    event.preventDefault();
    let allInputsAreNonEmpty = Object.values(inputDOMSelectors).every(
      (input) => input.value.trim() !== ""
    );

    if (!allInputsAreNonEmpty) {
      //   console.log("HAS INVALID");
      return;
    }
    // console.log("ALL ARE VALID");

    const { genre, name, author, date } = inputDOMSelectors;
    const songContainer = createElement(
      "div",
      otherDOMSelectors.allHitsContainer,
      "",
      ["hits-info"]
    );
    createElement("img", songContainer, null, null, null, {
      src: "./static/img/img.png",
    });
    createElement("h2", songContainer, `Genre: ${genre.value}`);
    createElement("h2", songContainer, `Name: ${name.value}`);
    createElement("h2", songContainer, `Author: ${author.value}`);
    createElement("h3", songContainer, `Date: ${date.value}`);
    const saveBtn = createElement("button", songContainer, "Save song", [
      "save-btn",
    ]);
    const likeBtn = createElement("button", songContainer, "Like song", [
      "like-btn",
    ]);
    const deleteBtn = createElement("button", songContainer, "Delete", [
      "delete-btn",
    ]);

    saveBtn.addEventListener("click", saveSongHandler);
    likeBtn.addEventListener("click", likeSongHandler);
    deleteBtn.addEventListener("click", deleteSongHandler);

    clearAllInputs();
  }

  function saveSongHandler() {
    const songRef = this.parentNode; // this is an object reference, based on row 78, the object will move
    const songCopy = this.parentNode.cloneNode(true); // this is the DOM object copy, the object will stay in both sections
    // console.dir(songRef);
    // console.log(this.parentNode);
    // console.log(songCopy);

    const saveBtn = songRef.querySelector(".save-btn");
    const likeBtn = songRef.querySelector(".like-btn");
    // const saveBtnC = songCopy.querySelector(".save-btn");
    // const likeBtnC = songCopy.querySelector(".like-btn");
    // const deleteBtnC = songCopy.querySelector(".delete-btn");
    // deleteBtnC.addEventListener("click", deleteSongHandler);

    otherDOMSelectors.savedContainer.appendChild(songRef);

    // otherDOMSelectors.savedContainer.appendChild(songCopy);

    saveBtn.remove();
    likeBtn.remove();
    // saveBtnC.remove();
    // likeBtnC.remove();
  }

  function likeSongHandler() {
    this.setAttribute("disabled", true);
    totalLikes++;
    otherDOMSelectors.totalLikesContainer.textContent = `Total Likes: ${totalLikes}`;
  }

  function deleteSongHandler() {
    this.parentNode.remove();
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
