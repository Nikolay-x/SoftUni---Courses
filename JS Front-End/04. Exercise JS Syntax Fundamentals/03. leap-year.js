// function leapYearD(year) {
//   if (year % 4 === 0 && year % 100 !== 0) {
//     console.log("yes");
//   } else if (year % 400 === 0) {
//     console.log("yes");
//   } else {
//     console.log("no");
//   }
// }

function leapYear(year) {
  if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
    console.log("yes");
  } else {
    console.log("no");
  }
}

// leapYearD(1984);
// leapYearD(2003);
// leapYearD(4);
// leapYearD(300);

leapYear(1984);
leapYear(2003);
leapYear(4);
leapYear(300);
