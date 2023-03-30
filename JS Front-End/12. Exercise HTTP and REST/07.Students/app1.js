function attachEvents() {
  const tBody = document.querySelector("#results > tbody");
  const firstNameInput = document.querySelector(
    "#form > div.inputs > input[type=text]:nth-child(1)"
  );
  const lastNameInput = document.querySelector(
    "#form > div.inputs > input[type=text]:nth-child(2)"
  );
  const facultyNumberInput = document.querySelector(
    "#form > div.inputs > input[type=text]:nth-child(3)"
  );
  const gradeInput = document.querySelector(
    "#form > div.inputs > input[type=text]:nth-child(4)"
  );
  const submitBtn = document.getElementById("submit");
  const BASE_URL = "http://localhost:3030/jsonstore/collections/students";

  submitBtn.addEventListener("click", submitHandler);

  async function loadStudents() {
    try {
      tBody.innerHTML = "";
      const studentsRes = await fetch(BASE_URL);
      const studentsData = await studentsRes.json();

      for (const studentId in studentsData) {
        const { firstName, lastName, facultyNumber, grade } =
          studentsData[studentId];
        const tableRow = document.createElement("tr");
        const firstNameColumn = document.createElement("td");
        const lastNameColumn = document.createElement("td");
        const facultyNumberColumn = document.createElement("td");
        const gradeColumn = document.createElement("td");

        firstNameColumn.textContent = firstName;
        lastNameColumn.textContent = lastName;
        facultyNumberColumn.textContent = facultyNumber;
        gradeColumn.textContent = grade;

        tableRow.appendChild(firstNameColumn);
        tableRow.appendChild(lastNameColumn);
        tableRow.appendChild(facultyNumberColumn);
        tableRow.appendChild(gradeColumn);

        tBody.appendChild(tableRow);
      }
    } catch (error) {}
  }

  loadStudents();

  async function submitHandler() {
    const firstName = firstNameInput.value;
    const lastName = lastNameInput.value;
    const facultyNumber = facultyNumberInput.value;
    const grade = gradeInput.value;
    const httpHeaders = {
      method: "POST",
      body: JSON.stringify({ firstName, lastName, facultyNumber, grade }),
    };
    const resData = await fetch(BASE_URL, httpHeaders);
    await loadStudents();

    firstNameInput.value = "";
    lastNameInput.value = "";
    facultyNumberInput.value = "";
    gradeInput.value = "";
  }
}

attachEvents();
