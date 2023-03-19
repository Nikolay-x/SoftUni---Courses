function solve() {
  document.querySelector("#btnSend").addEventListener("click", onClick);

  const textarea = document.getElementById("inputs").querySelector("textarea");
  const bestRestaurant = document.querySelector("#bestRestaurant > p");
  const workers = document.querySelector("#workers > p");

  let restaurantsInfo = {};
  bestRestaurant.textContent = "";
  workers.textContent = "";

  function onClick() {
    let inputsArr = Array.from(JSON.parse(textarea.value));
    //  console.log(inputsArr);

    for (const line of inputsArr) {
      let [restaurantName, workers] = line.split(" - ");
      if (!restaurantsInfo.hasOwnProperty(restaurantName)) {
        restaurantsInfo[restaurantName] = {};
      }
      workers.split(", ").map((worker) => {
        let [workerName, salary] = worker.split(" ");
        restaurantsInfo[restaurantName][workerName] = parseInt(salary);
      });
    }

    let bestR = null;
    let bestSum = null;

    for (let restaurant in restaurantsInfo) {
      let salary = Object.values(restaurantsInfo[restaurant]).map(Number);
      let avgSalary = salary.reduce((sum, num) => sum + num, 0) / salary.length;
      if (bestSum === null || avgSalary > bestSum) {
        bestSum = avgSalary;
        bestR = restaurant;
      }
    }

    let salary = Object.values(restaurantsInfo[bestR]).map(Number);
    bestRestaurant.textContent = `Name: ${bestR} Average Salary: ${(
      salary.reduce((sum, num) => sum + num, 0) / salary.length
    ).toFixed(2)} Best Salary: ${Math.max(...salary).toFixed(2)}`;
    let sortedWorkers = Object.entries(restaurantsInfo[bestR])
      .sort((a, b) => b[1] - a[1])
      .reduce((obj, [key, value]) => ({ ...obj, [key]: value }), {});

    for (const key in sortedWorkers) {
      workers.textContent += `Name: ${key} With Salary: ${sortedWorkers[key]} `;
    }
  }
}
