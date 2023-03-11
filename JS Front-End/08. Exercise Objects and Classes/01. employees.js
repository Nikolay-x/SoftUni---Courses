function employees(input) {
  let empls = {};
  for (let line of input) {
    empls[line] = line.length;
  }
  for (key in empls) {
    console.log(`Name: ${key} -- Personal Number: ${empls[key]}`);
  }
}

function employeesDemo(input) {
  Object.entries(
    input.reduce((data, employee) => {
      data[employee] = employee.length;
      return data;
    }, {})
  ).forEach(([employee, length]) => {
    console.log(`Name: ${employee} -- Personal Number: ${length}`);
  });
}

employees([
  "Silas Butler",
  "Adnaan Buckley",
  "Juan Peterson",
  "Brendan Villarreal",
]);

employees(["Samuel Jackson", "Will Smith", "Bruce Willis", "Tom Holland"]);

employees([
  "Silas Butler",
  "Adnaan Buckley",
  "Juan Peterson",
  "Brendan Villarreal",
]);

employeesDemo(["Samuel Jackson", "Will Smith", "Bruce Willis", "Tom Holland"]);
