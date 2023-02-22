// function solve(day, age) {
//   let ticketPrice;
//   if (day === "Weekday") {
//     if (0 <= age && age <= 18) {
//       ticketPrice = "12$";
//     } else if (18 < age && age <= 64) {
//       ticketPrice = "18$";
//     } else if (64 < age && age <= 122) {
//       ticketPrice = "12$";
//     } else {
//       ticketPrice = "Error!";
//     }
//   } else if (day === "Weekend") {
//     if (0 <= age && age <= 18) {
//       ticketPrice = "15$";
//     } else if (18 < age && age <= 64) {
//       ticketPrice = "20$";
//     } else if (64 < age && age <= 122) {
//       ticketPrice = "15$";
//     } else {
//       ticketPrice = "Error!";
//     }
//   } else if (day === "Holiday") {
//     if (0 <= age && age <= 18) {
//       ticketPrice = "5$";
//     } else if (18 < age && age <= 64) {
//       ticketPrice = "12$";
//     } else if (64 < age && age <= 122) {
//       ticketPrice = "10$";
//     } else {
//       ticketPrice = "Error!";
//     }
//   }
//   console.log(ticketPrice);
// }

function solveSwitch(day, age) {
  let ticketPrice;
  switch (day) {
    case "Weekday":
      if (0 <= age && age <= 18) {
        ticketPrice = "12$";
      } else if (18 < age && age <= 64) {
        ticketPrice = "18$";
      } else if (64 < age && age <= 122) {
        ticketPrice = "12$";
      } else {
        ticketPrice = "Error!";
      }
      break;
    case "Weekend":
      if (0 <= age && age <= 18) {
        ticketPrice = "15$";
      } else if (18 < age && age <= 64) {
        ticketPrice = "20$";
      } else if (64 < age && age <= 122) {
        ticketPrice = "15$";
      } else {
        ticketPrice = "Error!";
      }
      break;
    case "Holiday":
      if (0 <= age && age <= 18) {
        ticketPrice = "5$";
      } else if (18 < age && age <= 64) {
        ticketPrice = "12$";
      } else if (64 < age && age <= 122) {
        ticketPrice = "10$";
      } else {
        ticketPrice = "Error!";
      }
      break;
  }
  console.log(ticketPrice);
}

// solve("Weekday", 42);
// solve("Holiday", -12);
// solve("Holiday", 15);

solveSwitch("Weekday", 42);
solveSwitch("Holiday", -12);
solveSwitch("Holiday", 15);
