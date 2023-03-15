function armiesList(list) {
  let armies = {};
  for (const line of list) {
    if (line.includes("arrives")) {
      let leader = line.split(" arrives")[0];
      if (!armies.hasOwnProperty(leader)) {
        armies[leader] = {};
        armies[leader].totalCount = 0;
        armies[leader].armiesList = [];
      }
    } else if (line.includes(":")) {
      [leader, ...army] = line.split(": ");
      let [armyName, armyCount] = army[0].split(", ");
      if (armies.hasOwnProperty(leader)) {
        armies[leader].totalCount += Number(armyCount);
        armies[leader].armiesList.push({
          name: armyName,
          count: Number(armyCount),
        });
      }
    } else if (line.includes("+")) {
      let [armyName, count] = line.split(" + ");
      for (leader in armies) {
        armies[leader].armiesList.forEach((army) => {
          if (army.name == armyName) {
            count = Number(count);
            army.count += count;
            armies[leader].totalCount += count;
          }
        });
      }
    } else if (line.includes("defeated")) {
      let leader = line.split(" defeated")[0];
      if (armies.hasOwnProperty(leader)) {
        delete armies[leader];
      }
    }
  }

  for (const [name, army] of Object.entries(armies).sort(
    ([, a], [, b]) => b.totalCount - a.totalCount
  )) {
    console.log(`${name}: ${army.totalCount}`);

    for (const { name, count } of army.armiesList.sort(
      (a, b) => b.count - a.count
    )) {
      console.log(`>>> ${name} - ${count}`);
    }
  }
}

function armiesL(list) {
  let armies = {};
  for (const line of list) {
    if (line.includes("arrives")) {
      let leader = line.split(" arrives")[0];
      armies[leader] = {};
      armies[leader].totalCount = 0;
      armies[leader].armiesList = [];
    } else if (line.includes(":")) {
      let [leader, army] = line.split(": ");
      let [armyName, armyCount] = army.split(", ");
      if (armies.hasOwnProperty(leader)) {
        armies[leader].totalCount += Number(armyCount);
        armies[leader].armiesList.push([armyName, Number(armyCount)]);
      }
    } else if (line.includes("+")) {
      let [armyName, count] = line.split(" + ");
      for (leader in armies) {
        armies[leader].armiesList.forEach((army) => {
          if (army[0] === armyName) {
            armies[leader].totalCount += Number(count);
            army[1] += Number(count);
          }
        });
      }
    } else if (line.includes("defeated")) {
      let leader = line.split(" defeated")[0];
      if (armies.hasOwnProperty(leader)) {
        delete armies[leader];
      }
    }
  }

  let sortedArmies = Object.entries(armies).sort(
    (leader1, leader2) => leader2[1].totalCount - leader1[1].totalCount
  );

  for (const entry of sortedArmies) {
    console.log(`${entry[0]}: ${entry[1].totalCount}`);
    let sortedArmy = entry[1].armiesList.sort((a, b) => b[1] - a[1]);
    for (const army of sortedArmy) {
      console.log(`>>> ${army[0]} - ${army[1]}`);
    }
  }
}

armiesList([
  "Rick Burr arrives",
  "Fergus: Wexamp, 30245",
  "Rick Burr: Juard, 50000",
  "Findlay arrives",
  "Findlay: Britox, 34540",
  "Wexamp + 6000",
  "Juard + 1350",
  "Britox + 4500",
  "Porter arrives",
  "Porter: Legion, 55000",
  "Legion + 302",
  "Rick Burr defeated",
  "Porter: Retix, 3205",
]);

armiesList([
  "Rick Burr arrives",
  "Findlay arrives",
  "Rick Burr: Juard, 1500",
  "Wexamp arrives",
  "Findlay: Wexamp, 34540",
  "Wexamp + 340",
  "Wexamp: Britox, 1155",
  "Wexamp: Juard, 43423",
]);

armiesList([
  "A arrives",
  "A: L, 30245",
  "A: B, 50000",
  "C arrives",
  "B + 34540",
  "L + 340",
]);

// armiesL([
//   "Rick Burr arrives",
//   "Fergus: Wexamp, 30245",
//   "Rick Burr: Juard, 50000",
//   "Findlay arrives",
//   "Findlay: Britox, 34540",
//   "Wexamp + 6000",
//   "Juard + 1350",
//   "Britox + 4500",
//   "Porter arrives",
//   "Porter: Legion, 55000",
//   "Legion + 302",
//   "Rick Burr defeated",
//   "Porter: Retix, 3205",
// ]);

// armiesL([
//   "Rick Burr arrives",
//   "Findlay arrives",
//   "Rick Burr: Juard, 1500",
//   "Wexamp arrives",
//   "Findlay: Wexamp, 34540",
//   "Wexamp + 340",
//   "Wexamp: Britox, 1155",
//   "Wexamp: Juard, 43423",
// ]);

armiesL([
  "A arrives",
  "A: L, 30245",
  "A: B, 50000",
  "C arrives",
  "B + 34540",
  "L + 340",
]);
