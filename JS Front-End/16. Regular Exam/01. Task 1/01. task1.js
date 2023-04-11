function sprintBoardArr(input) {
  let n = Number(input.shift());
  // console.log(n);
  // console.log(input);

  let sprintBoard = {};
  let toDoTasksTotalPoints = 0;
  let inProgressTasksTotalPoints = 0;
  let codeReviewTasksTotalPoints = 0;
  let doneTasksTotalPoints = 0;

  let commandParser = {
    "Add New": addTask,
    "Change Status": changeStatus,
    "Remove Task": removeTask,
  };

  for (let i = 0; i < n; i++) {
    const [assignee, taskId, title, status, estimatedPoints] = input
      .shift()
      .split(":");

    if (!sprintBoard.hasOwnProperty(assignee)) {
      sprintBoard[assignee] = [[taskId, title, status, estimatedPoints]];
    } else {
      sprintBoard[assignee].push([taskId, title, status, estimatedPoints]);
    }
  }
  // console.log(sprintBoard);

  for (const inputLine of input) {
    let commandTokens = inputLine.split(":");
    let command = commandTokens[0];
    commandParser[command](...commandTokens.slice(1));
  }
  // console.log(sprintBoard);

  for (const assignee in sprintBoard) {
    for (const task of sprintBoard[assignee]) {
      if (task[2] === "ToDo") {
        toDoTasksTotalPoints += Number(task[3]);
      } else if (task[2] === "In Progress") {
        inProgressTasksTotalPoints += Number(task[3]);
      } else if (task[2] === "Code Review") {
        codeReviewTasksTotalPoints += Number(task[3]);
      } else if (task[2] === "Done") {
        doneTasksTotalPoints += Number(task[3]);
      }
    }
  }

  console.log(`ToDo: ${toDoTasksTotalPoints}pts`);
  console.log(`In Progress: ${inProgressTasksTotalPoints}pts`);
  console.log(`Code Review: ${codeReviewTasksTotalPoints}pts`);
  console.log(`Done Points: ${doneTasksTotalPoints}pts`);

  let notDonePoints =
    toDoTasksTotalPoints +
    inProgressTasksTotalPoints +
    codeReviewTasksTotalPoints;

  if (doneTasksTotalPoints >= notDonePoints) {
    console.log("Sprint was successful!");
  } else {
    console.log("Sprint was unsuccessful...");
  }

  function addTask(assignee, taskId, title, status, estimatedPoints) {
    if (sprintBoard.hasOwnProperty(assignee)) {
      sprintBoard[assignee].push([taskId, title, status, estimatedPoints]);
    } else {
      console.log(`Assignee ${assignee} does not exist on the board!`);
    }
  }

  function changeStatus(assignee, taskId, newStatus) {
    if (!sprintBoard.hasOwnProperty(assignee)) {
      console.log(`Assignee ${assignee} does not exist on the board!`);
      return;
    }

    let task = sprintBoard[assignee].find((t) => t[0] === taskId);

    if (!task) {
      console.log(`Task with ID ${taskId} does not exist for ${assignee}!`);
      return;
    }

    task.splice(2, 1, newStatus);
  }

  function removeTask(assignee, index) {
    if (!sprintBoard.hasOwnProperty(assignee)) {
      console.log(`Assignee ${assignee} does not exist on the board!`);
      return;
    }

    if (index < 0 || index >= sprintBoard[assignee].length) {
      console.log(`Index is out of range!`);
      return;
    }

    // console.log(sprintBoard[assignee].length);

    sprintBoard[assignee].splice(index, 1);
  }
}

function sprintBoardObj(input) {
  let n = Number(input.shift());

  let sprintBoard = {};
  let toDoTasksTotalPoints = 0;
  let inProgressTasksTotalPoints = 0;
  let codeReviewTasksTotalPoints = 0;
  let doneTasksTotalPoints = 0;

  let commandParser = {
    "Add New": addTask,
    "Change Status": changeStatus,
    "Remove Task": removeTask,
  };

  for (let i = 0; i < n; i++) {
    const [assignee, taskId, title, status, estimatedPoints] = input
      .shift()
      .split(":");

    if (!sprintBoard.hasOwnProperty(assignee)) {
      sprintBoard[assignee] = [{ taskId, title, status, estimatedPoints }];
    } else {
      sprintBoard[assignee].push({ taskId, title, status, estimatedPoints });
    }
  }

  for (const inputLine of input) {
    let commandTokens = inputLine.split(":");
    let command = commandTokens[0];
    commandParser[command](...commandTokens.slice(1));
  }

  for (const assignee in sprintBoard) {
    for (const task of sprintBoard[assignee]) {
      if (task.status === "ToDo") {
        toDoTasksTotalPoints += Number(task.estimatedPoints);
      } else if (task.status === "In Progress") {
        inProgressTasksTotalPoints += Number(task.estimatedPoints);
      } else if (task.status === "Code Review") {
        codeReviewTasksTotalPoints += Number(task.estimatedPoints);
      } else if (task.status === "Done") {
        doneTasksTotalPoints += Number(task.estimatedPoints);
      }
    }
  }

  console.log(`ToDo: ${toDoTasksTotalPoints}pts`);
  console.log(`In Progress: ${inProgressTasksTotalPoints}pts`);
  console.log(`Code Review: ${codeReviewTasksTotalPoints}pts`);
  console.log(`Done Points: ${doneTasksTotalPoints}pts`);

  let notDonePoints =
    toDoTasksTotalPoints +
    inProgressTasksTotalPoints +
    codeReviewTasksTotalPoints;

  if (doneTasksTotalPoints >= notDonePoints) {
    console.log("Sprint was successful!");
  } else {
    console.log("Sprint was unsuccessful...");
  }

  function addTask(assignee, taskId, title, status, estimatedPoints) {
    if (sprintBoard.hasOwnProperty(assignee)) {
      sprintBoard[assignee].push({ taskId, title, status, estimatedPoints });
    } else {
      console.log(`Assignee ${assignee} does not exist on the board!`);
    }
  }

  function changeStatus(assignee, taskId, newStatus) {
    if (!sprintBoard.hasOwnProperty(assignee)) {
      console.log(`Assignee ${assignee} does not exist on the board!`);
      return;
    }

    let task = sprintBoard[assignee].find((t) => t.taskId === taskId);

    if (!task) {
      console.log(`Task with ID ${taskId} does not exist for ${assignee}!`);
      return;
    }

    task.status = newStatus;
  }

  function removeTask(assignee, index) {
    if (!sprintBoard.hasOwnProperty(assignee)) {
      console.log(`Assignee ${assignee} does not exist on the board!`);
      return;
    }

    if (index < 0 || index >= sprintBoard[assignee].length) {
      console.log(`Index is out of range!`);
      return;
    }

    sprintBoard[assignee].splice(index, 1);
  }
}

// sprintBoardArr([
//   "5",
//   "Kiril:BOP-1209:Fix Minor Bug:ToDo:3",
//   "Mariya:BOP-1210:Fix Major Bug:In Progress:3",
//   "Peter:BOP-1211:POC:Code Review:5",
//   "Georgi:BOP-1212:Investigation Task:Done:2",
//   "Mariya:BOP-1213:New Account Page:In Progress:13",
//   "Add New:Kiril:BOP-1217:Add Info Page:In Progress:5",
//   "Change Status:Peter:BOP-1290:ToDo",
//   "Remove Task:Mariya:1",
//   // "Remove Task:Mariya:4",
//   "Remove Task:Joro:1",
// ]);

sprintBoardObj([
  "5",
  "Kiril:BOP-1209:Fix Minor Bug:ToDo:3",
  "Mariya:BOP-1210:Fix Major Bug:In Progress:3",
  "Peter:BOP-1211:POC:Code Review:5",
  "Georgi:BOP-1212:Investigation Task:Done:2",
  "Mariya:BOP-1213:New Account Page:In Progress:13",
  "Add New:Kiril:BOP-1217:Add Info Page:In Progress:5",
  "Change Status:Peter:BOP-1290:ToDo",
  "Remove Task:Mariya:1",
  "Remove Task:Joro:1",
]);

// sprintBoardArr([
//   "4",
//   "Kiril:BOP-1213:Fix Typo:Done:1",
//   "Peter:BOP-1214:New Products Page:In Progress:2",
//   "Mariya:BOP-1215:Setup Routing:ToDo:8",
//   "Georgi:BOP-1216:Add Business Card:Code Review:3",
//   "Add New:Sam:BOP-1237:Testing Home Page:Done:3",
//   "Change Status:Georgi:BOP-1216:Done",
//   "Change Status:Will:BOP-1212:In Progress",
//   "Remove Task:Georgi:3",
//   "Change Status:Mariya:BOP-1215:Done",
// ]);
