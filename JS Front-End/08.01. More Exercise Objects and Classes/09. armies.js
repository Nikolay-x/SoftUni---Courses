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
