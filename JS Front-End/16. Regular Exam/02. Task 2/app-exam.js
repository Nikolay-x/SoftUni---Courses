window.addEventListener("load", solve);

function solve() {
  let totalPoints = 0;
  let taskIdStart = 1;

  let currentTasks = [];
  let taskToEdit = {};

  const htmlIcons = {
    Feature: "&#8865",
    "Low Priority Bug": "&#9737",
    "High Priority Bug": "&#9888",
  };

  const addClass = {
    Feature: "feature",
    "Low Priority Bug": "low-priority",
    "High Priority Bug": "high-priority",
  };

  const inputDOMSelectors = {
    taskSelectorId: document.getElementById("task-id"),
    title: document.getElementById("title"),
    description: document.getElementById("description"),
    label: document.getElementById("label"),
    points: document.getElementById("points"),
    assignee: document.getElementById("assignee"),
  };

  const otherDOMSelectors = {
    newSprintTasks: document.getElementById("tasks-section"),
    totalPointsField: document.getElementById("total-sprint-points"),
    createTaskBtn: document.getElementById("create-task-btn"),
    deleteTaskBtn: document.getElementById("delete-task-btn"),
  };

  otherDOMSelectors.createTaskBtn.addEventListener("click", createTaskHandler);
  otherDOMSelectors.deleteTaskBtn.addEventListener("click", deleteTaskHandler);

  function createTaskHandler(event) {
    let taskId = taskIdStart;
    if (event) {
      event.preventDefault();
    }

    inputDOMSelectors.taskSelectorId.value = taskId;

    let allInputsAreNonEmpty = Object.values(inputDOMSelectors).every(
      (input) => input.value.trim() !== ""
    );

    if (!allInputsAreNonEmpty) {
      return;
    }

    const { taskSelectorId, title, description, label, points, assignee } =
      inputDOMSelectors;

    currentTasks.push({
      taskSelectorId,
      title,
      description,
      label,
      points,
      assignee,
    });

    const taskContainer = createElement(
      "article",
      otherDOMSelectors.newSprintTasks,
      null,
      ["task-card"],
      `task-${taskId}`
    );
    taskContainer.id = taskId;
    createElement(
      "div",
      taskContainer,
      `${label.value} ${htmlIcons[label.value]}`,
      ["task-card-label", `${addClass[label.value]}`],
      null,
      null,
      true
    );
    createElement("h3", taskContainer, `${title.value}`, ["task-card-title"]);
    createElement("p", taskContainer, `${description.value}`, [
      "task-card-description",
    ]);
    createElement("div", taskContainer, `Estimated at ${points.value} pts`, [
      "task-card-points",
    ]);
    createElement("div", taskContainer, `Assigned to: ${assignee.value}`, [
      "task-card-assignee",
    ]);
    const deleteDiv = createElement("div", taskContainer, null, [
      "task-card-actions",
    ]);
    const taskDeleteBtn = createElement("button", deleteDiv, "Delete");

    taskDeleteBtn.addEventListener("click", internalDeleteTaskHandler);

    taskIdStart += 1;
    totalPoints += Number(points.value);
    otherDOMSelectors.totalPointsField.textContent = `Total Points ${totalPoints}pts`;

    clearAllInputs();
  }

  function deleteTaskHandler() {}

  function internalDeleteTaskHandler() {
    let id = this.parentNode.parentNode.id;
    taskToEdit = currentTasks.find((t) => t.idObj === id);

    for (const key in inputDOMSelectors) {
      inputDOMSelectors[key].value = taskToEdit[key];
      inputDOMSelectors[key].setAttribute("disabled", true);
    }

    otherDOMSelectors.createTaskBtn.setAttribute("disabled", true);
    otherDOMSelectors.deleteTaskBtn.removeAttribute("disabled");
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
