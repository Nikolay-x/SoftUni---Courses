// TODO:
function attachEvents() {
  const BASE_URL = "http://localhost:3030/jsonstore/tasks/";

  const inputDOMSelectors = {
    title: document.getElementById("title"),
    description: document.getElementById("description"),
  };

  const otherDOMSelectors = {
    loadBoardBtn: document.getElementById("load-board-btn"),
    createTaskBtn: document.getElementById("create-task-btn"),
    toDoSection: document.querySelector("#todo-section > ul"),
    inProgressSection: document.querySelector("#in-progress-section > ul"),
    codeReviewSection: document.querySelector("#code-review-section > ul"),
    doneSection: document.querySelector("#done-section > ul"),
  };

  let currentTasksState = [];
  let taskToMove = {};

  otherDOMSelectors.loadBoardBtn.addEventListener("click", loadBoardHandler);
  otherDOMSelectors.createTaskBtn.addEventListener("click", createTaskHandler);

  function loadBoardHandler(event) {
    if (event) {
      event.preventDefault();
    }

    if (otherDOMSelectors.toDoSection) {
      otherDOMSelectors.toDoSection.innerHTML = "";
    }
    if (otherDOMSelectors.inProgressSection) {
      otherDOMSelectors.inProgressSection.innerHTML = "";
    }
    if (otherDOMSelectors.codeReviewSection) {
      otherDOMSelectors.codeReviewSection.innerHTML = "";
    }
    if (otherDOMSelectors.doneSection) {
      otherDOMSelectors.doneSection.innerHTML = "";
    }

    fetch(BASE_URL)
      .then((res) => res.json())
      .then((allTasksRes) => {
        currentTasks = Object.values(allTasksRes);

        let parentContainer = null;
        let btnContent = "";

        for (const { title, description, status, _id } of currentTasks) {
          currentTasksState.push({ title, description, status, _id });

          if (status === "ToDo") {
            parentContainer = otherDOMSelectors.toDoSection;
            btnContent = "Move to In Progress";
          } else if (status === "In Progress") {
            parentContainer = otherDOMSelectors.inProgressSection;
            btnContent = "Move to Code Review";
          } else if (status === "Code Review") {
            parentContainer = otherDOMSelectors.codeReviewSection;
            btnContent = "Move to Done";
          } else if (status === "Done") {
            parentContainer = otherDOMSelectors.doneSection;
            btnContent = "Close";
          }

          const taskLi = createElement("li", parentContainer, null, ["task"]);
          taskLi.id = _id;
          createElement("h3", taskLi, `${title}`);
          createElement("p", taskLi, `${description}`);
          const statusBtn = createElement("button", taskLi, `${btnContent}`);

          statusBtn.addEventListener("click", statusHandler);
        }
      })
      .catch((err) => {
        console.error(err);
      });
  }

  function createTaskHandler(event) {
    if (event) {
      event.preventDefault();
    }

    const { title, description } = inputDOMSelectors;
    const payload = JSON.stringify({
      title: title.value,
      description: description.value,
      status: "ToDo",
    });
    const httpHeaders = {
      method: "POST",
      body: payload,
    };

    fetch(BASE_URL, httpHeaders)
      .then(() => {
        loadBoardHandler();
        clearAllInputs();
      })
      .catch((err) => {
        console.error(err);
      });
  }

  function statusHandler(event) {
    if (event) {
      event.preventDefault();
    }

    const id = this.parentNode.id;
    parentLi = this.parentNode;
    btn = this;
    btnContent = this.textContent;
    // console.log(btnContent);
    let newStatus = null;

    // taskToMove = currentTasksState.find((t) => (t._id = id));
    // console.log(taskToMove);

    if (btnContent === "Move to In Progress") {
      btnContent = "Move to Code Review";
      newStatus = "In Progress";
    } else if (btnContent === "Move to Code Review") {
      btnContent = "Move to Done";
      newStatus = "Code Review";
    } else if (btnContent === "Move to Done") {
      btnContent = "CloseTo";
      newStatus = "Done";
    }

    const payload = JSON.stringify({
      status: newStatus,
    });

    let httpHeaders = { method: "PATCH", body: payload };

    if (btnContent === "Close") {
      httpHeaders.method = "DELETE";
    }

    fetch(`${BASE_URL}${id}`, httpHeaders)
      .then(() => {
        btn.textContent = btnContent;
        if (btn.textContent === "CloseTo") {
          btn.textContent = "Close";
        }
        loadBoardHandler();
      })
      .catch((err) => {
        console.error(err);
      });
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

attachEvents();
