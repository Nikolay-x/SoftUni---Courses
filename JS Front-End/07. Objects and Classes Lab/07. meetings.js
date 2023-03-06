function meetings(dataArr) {
  let meetingsBoard = {};
  for (let entry of dataArr) {
    let entryParts = entry.split(" ");
    let weekday = entryParts[0];
    let name = entryParts[1];
    // let [weekday, name] = entry.split(" ");

    if (meetingsBoard.hasOwnProperty(weekday)) {
      console.log(`Conflict on ${weekday}!`);
    } else {
      meetingsBoard[weekday] = name;
      console.log(`Scheduled for ${weekday}`);
    }
  }
  for (key in meetingsBoard) {
    console.log(`${key} -> ${meetingsBoard[key]}`);
  }
}

meetings(["Monday Peter", "Wednesday Bill", "Monday Tim", "Friday Tim"]);
meetings([
  "Friday Bob",
  "Saturday Ted",
  "Monday Bill",
  "Monday John",
  "Wednesday George",
]);
