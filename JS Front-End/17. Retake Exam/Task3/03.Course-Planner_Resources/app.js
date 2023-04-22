function attachEvents() {
  const BASE_URL = "http://localhost:3030/jsonstore/tasks/";
  const inputDOMSelectors = {
    title: document.getElementById("course-name"),
    type: document.getElementById("course-type"),
    description: document.getElementById("description"),
    teacher: document.getElementById("teacher-name"),
  };
  const otherDOMSelectors = {
    addBtn: document.getElementById("add-course"),
    editBtn: document.getElementById("edit-course"),
    loadBtn: document.getElementById("load-course"),
    coursesContainer: document.getElementById("list"),
  };

  let currentCourses = [];
  let courseToEdit = {};

  otherDOMSelectors.loadBtn.addEventListener("click", loadAllHandler);
  otherDOMSelectors.editBtn.addEventListener("click", editHandler);
  otherDOMSelectors.addBtn.addEventListener("click", addHandler);

  function loadAllHandler(event) {
    if (event) {
      event.preventDefault();
    }

    otherDOMSelectors.coursesContainer.innerHTML = "";

    fetch(BASE_URL)
      .then((res) => res.json())
      .then((allCoursesRes) => {
        currentCourses = Object.values(allCoursesRes);
        // console.log(currentCourses);

        for (const {
          title,
          type,
          description,
          teacher,
          _id,
        } of currentCourses) {
          const divParent = createElement(
            "div",
            otherDOMSelectors.coursesContainer,
            "",
            ["container"]
          );
          divParent.id = _id;

          createElement("h2", divParent, `${title}`);
          createElement("h3", divParent, `${teacher}`);
          createElement("h3", divParent, `${type}`);
          createElement("h4", divParent, `${description}`);

          const editCourseBtn = createElement(
            "button",
            divParent,
            "Edit Course",
            ["edit-btn"]
          );

          const finishCourseBtn = createElement(
            "button",
            divParent,
            "Finish Course",
            ["finish-btn"]
          );

          editCourseBtn.addEventListener("click", loadUpdateFormHandler);
          finishCourseBtn.addEventListener("click", finishCourseHandler);
        }
      });
  }

  function loadUpdateFormHandler() {
    const id = this.parentNode.id;

    courseToEdit = currentCourses.find((c) => c._id === id);

    for (const key in inputDOMSelectors) {
      inputDOMSelectors[key].value = courseToEdit[key];
    }

    otherDOMSelectors.addBtn.setAttribute("disabled", true);
    otherDOMSelectors.editBtn.removeAttribute("disabled");

    this.parentNode.remove();
  }

  function finishCourseHandler() {
    const id = this.parentNode.id;
    const httpHeaders = {
      method: "DELETE",
    };

    fetch(`${BASE_URL}${id}`, httpHeaders)
      .then(() => {
        loadAllHandler();
      })
      .catch((err) => console.error(err));
  }

  function editHandler(event) {
    if (event) {
      event.preventDefault();
    }

    const { title, type, description, teacher } = inputDOMSelectors;
    const payload = JSON.stringify({
      title: title.value,
      type: type.value,
      description: description.value,
      teacher: teacher.value,
      _id: courseToEdit._id,
    });
    const httpHeaders = {
      method: "PUT",
      body: payload,
    };

    fetch(`${BASE_URL}${courseToEdit._id}`, httpHeaders)
      .then(() => {
        loadAllHandler();
        otherDOMSelectors.addBtn.removeAttribute("disabled");
        otherDOMSelectors.editBtn.setAttribute("disabled", true);
        clearAllInputs();
      })
      .catch((err) => {
        console.error(err);
      });
  }

  function addHandler(event) {
    if (event) {
      event.preventDefault();
    }
    const { title, type, description, teacher } = inputDOMSelectors;
    const payload = JSON.stringify({
      title: title.value,
      type: type.value,
      description: description.value,
      teacher: teacher.value,
    });
    const httpHeaders = {
      method: "POST",
      body: payload,
    };

    fetch(BASE_URL, httpHeaders)
      .then(() => {
        loadAllHandler();
        clearAllInputs();
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
