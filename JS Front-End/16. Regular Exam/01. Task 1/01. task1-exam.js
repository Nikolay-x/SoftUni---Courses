function solve(input) {
  let n = Number(input.shift());
  let board = {};

  for (let i = 0; i < n; i++) {
    let [assignee, taskId, title, status, estimatedPoints] =
      input[i].split(":");
    estimatedPoints = Number(estimatedPoints);
    if (!board.hasOwnProperty(assignee)) {
      board[assignee] = [];
    }
    board[assignee].push({ taskId, title, status, estimatedPoints });
  }

  let commands = input.slice(n);

  for (let command of commands) {
    let [action, assignee, idOrIndex, newStatus] = command.split(":");

    if (action === "Add New") {
      let estimatedPoints = Number(newStatus);
      newStatus = idOrIndex;
      let taskId = new Date().getTime().toString();
      if (!board.hasOwnProperty(assignee)) {
        console.log(`Assignee ${assignee} does not exist on the board!`);
        continue;
      }
      board[assignee].push({
        taskId,
        title: newStatus,
        status: newStatus,
        estimatedPoints,
      });
    }

    if (action === "Change Status") {
      let taskId = idOrIndex;
      let index = board[assignee].findIndex((task) => task.taskId === taskId);
      if (index === -1) {
        console.log(`Task with ID ${taskId} does not exist for ${assignee}!`);
        continue;
      }
      let estimatedPoints = board[assignee][index].estimatedPoints;
      board[assignee][index] = {
        taskId,
        title: newStatus,
        status: newStatus,
        estimatedPoints,
      };
    }

    if (action === "Remove Task") {
      let index = Number(idOrIndex);
      if (!board.hasOwnProperty(assignee)) {
        console.log(`Assignee ${assignee} does not exist on the board!`);
        continue;
      }
      if (index < 0 || index >= board[assignee].length) {
        console.log(`Index is out of range!`);
        continue;
      }
      board[assignee].splice(index, 1);
    }
  }

  let toDoTasksTotalPoints = 0;
  let inProgressTasksTotalPoints = 0;
  let codeReviewTasksTotalPoints = 0;
  let doneTasksTotalPoints = 0;

  for (let assignee in board) {
    for (let task of board[assignee]) {
      switch (task.status) {
        case "ToDo":
          toDoTasksTotalPoints += task.estimatedPoints;
          break;
        case "In Progress":
          inProgressTasksTotalPoints += task.estimatedPoints;
          break;
        case "Code Review":
          codeReviewTasksTotalPoints += task.estimatedPoints;
          break;
        case "Done":
          doneTasksTotalPoints += task.estimatedPoints;
          break;
      }
    }
  }

  console.log(`ToDo: ${toDoTasksTotalPoints}pts`);
  console.log(`In Progress: ${inProgressTasksTotalPoints}pts`);
  console.log(`Code Review: ${codeReviewTasksTotalPoints}pts`);
  console.log(`Done Points: ${doneTasksTotalPoints}pts`);

  if (
    doneTasksTotalPoints >=
    toDoTasksTotalPoints +
      inProgressTasksTotalPoints +
      codeReviewTasksTotalPoints
  ) {
    console.log(`Sprint was successful!`);
  } else {
    console.log(`Sprint was unsuccessful...`);
  }
}

solve([
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
