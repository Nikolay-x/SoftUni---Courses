window.addEventListener("load", solve);

function solve() {
  const ticketState = {
    firstName: null,
    lastName: null,
    peopleCount: null,
    fromDate: null,
    daysCount: null,
  };

  const inputDOMSelectors = {
    firstName: document.getElementById("first-name"),
    lastName: document.getElementById("last-name"),
    peopleCount: document.getElementById("people-count"),
    fromDate: document.getElementById("from-date"),
    daysCount: document.getElementById("days-count"),
  };

  const otherDOMSelectors = {
    nextBtn: document.getElementById("next-btn"),
    ticketPreviewContainer: document.querySelector(
      "#info-ticket > div > div > ul"
    ),
    form: document.querySelector("#append-ticket > div > div > form"),
    confirmTicketContainer: document.querySelector(
      "#confirm-ticket-section > div > div > ul"
    ),
    main: document.getElementById("main"),
    body: document.getElementById("body"),
  };

  otherDOMSelectors.nextBtn.addEventListener("click", nextStepHandler);

  function nextStepHandler(event) {
    if (event) {
      event.preventDefault();
    }

    let allInputsAreNonEmpty = Object.values(inputDOMSelectors).every(
      (input) => input.value.trim() !== ""
    );

    if (!allInputsAreNonEmpty) {
      console.log("invalid input");
      return;
    }

    const { firstName, lastName, peopleCount, fromDate, daysCount } =
      inputDOMSelectors;

    const liTicket = createElement(
      "li",
      otherDOMSelectors.ticketPreviewContainer,
      null,
      ["ticket"]
    );
    const article = createElement("article", liTicket);
    createElement("h3", article, `Name: ${firstName.value} ${lastName.value}`);
    createElement("p", article, `From date: ${fromDate.value}`);
    createElement("p", article, `For ${daysCount.value} days`);
    createElement("p", article, `For ${peopleCount.value} people`);
    const editBtn = createElement("button", liTicket, "Edit", ["edit-btn"]);
    const continueBtn = createElement("button", liTicket, "Continue", [
      "continue-btn",
    ]);

    editBtn.addEventListener("click", editTicketHandler);
    continueBtn.addEventListener("click", continueTicketHandler);

    for (const key in inputDOMSelectors) {
      ticketState[key] = inputDOMSelectors[key].value;
    }

    otherDOMSelectors.form.reset();

    otherDOMSelectors.nextBtn.setAttribute("disabled", true);
  }

  function editTicketHandler() {
    for (const key in inputDOMSelectors) {
      inputDOMSelectors[key].value = ticketState[key];
    }
    otherDOMSelectors.ticketPreviewContainer.innerHTML = "";
    otherDOMSelectors.nextBtn.removeAttribute("disabled");
  }

  function continueTicketHandler() {
    const ticketRef = this.parentNode;
    const editBtn = ticketRef.querySelector(".edit-btn");
    const continueBtn = ticketRef.querySelector(".continue-btn");

    const confirmBtn = createElement("button", ticketRef, "Confirm", [
      "confirm-btn",
    ]);
    const cancelBtn = createElement("button", ticketRef, "Cancel", [
      "cancel-btn",
    ]);

    confirmBtn.addEventListener("click", confirmHandler);
    cancelBtn.addEventListener("click", cancelHandler);

    otherDOMSelectors.confirmTicketContainer.appendChild(ticketRef);

    editBtn.remove();
    continueBtn.remove();
  }

  function confirmHandler() {
    otherDOMSelectors.main.remove();
    createElement(
      "h1",
      otherDOMSelectors.body,
      "Thank you, have a nice day! ",
      null,
      "thank-you"
    );
    const backBtn = createElement(
      "button",
      otherDOMSelectors.body,
      "Back",
      null,
      "back-btn"
    );

    backBtn.addEventListener("click", backHandler);
  }

  function cancelHandler() {
    this.parentNode.remove();
    otherDOMSelectors.nextBtn.removeAttribute("disabled");
  }

  function backHandler() {
    window.location.reload();
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
