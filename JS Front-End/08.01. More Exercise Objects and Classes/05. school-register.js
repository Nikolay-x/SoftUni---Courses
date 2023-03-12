function school(inputArr) {
  let students = [];
  for (const line of inputArr) {
    let name = line.split(", ")[0].split(": ")[1];
    let grade = line.split(", ")[1].split(": ")[1];
    let score = line.split(", ")[2].split(": ")[1];
    if (score >= 3) {
      students.push({ name, grade, score });
    }
  }
  let sortedStudents = students.sort(
    (a, b) => Number(a.grade) - Number(b.grade)
  );

  let grade = "";
  let output = [];
  let studentList = [];
  let totalScore = 0;
  for (const student of sortedStudents) {
    let currentGrade = student.grade;
    if (grade !== currentGrade) {
      output.push(grade);
      output.push(studentList);
      output.push((totalScore / studentList.length).toFixed(2));
      studentList = [];
      totalScore = 0;
      grade = currentGrade;
    }
    studentList.push(student.name);
    totalScore += Number(student.score);
  }
  output.push(grade);
  output.push(studentList);
  output.push((totalScore / studentList.length).toFixed(2));

  output = output.slice(3);

  for (let i = 0; i < output.length; i += 3) {
    console.log(`${Number(output[i]) + 1} Grade`);
    console.log(`List of students: ${output[i + 1].join(", ")}`);
    console.log(`Average annual score from last year: ${output[i + 2]}`);
    console.log("");
  }
}

// function school(list) {
//   studentsObj = {};

//   for (item of list) {
//     let [name, grade, avrScore] = item.split(", ");
//     name = name.split(": ")[1];
//     grade = parseInt(grade.split(": ")[1]);
//     avrScore = parseFloat(avrScore.split(": ")[1]);
//     if (avrScore >= 3) {
//       grade += 1;
//       if (!studentsObj.hasOwnProperty(grade)) {
//         studentsObj[grade] = {};
//         studentsObj[grade].students = [];
//         studentsObj[grade].totalScore = 0;
//       }
//       studentsObj[grade].students.push(name);
//       studentsObj[grade].totalScore += avrScore;
//     }
//   }
//   for (entry of Object.entries(studentsObj)) {
//     console.log(`${entry[0]} Grade`);
//     console.log(`List of students: ${entry[1].students.join(", ")}`);
//     console.log(
//       `Average annual score from last year: ${(
//         entry[1].totalScore / entry[1].students.length
//       ).toFixed(2)}\n`
//     );
//   }
// }

school([
  "Student name: Mark, Grade: 8, Graduated with an average score: 4.75",
  "Student name: Ethan, Grade: 9, Graduated with an average score: 5.66",
  "Student name: George, Grade: 8, Graduated with an average score: 2.83",
  "Student name: Steven, Grade: 10, Graduated with an average score: 4.20",
  "Student name: Joey, Grade: 9, Graduated with an average score: 4.90",
  "Student name: Angus, Grade: 11, Graduated with an average score: 2.90",
  "Student name: Bob, Grade: 11, Graduated with an average score: 5.15",
  "Student name: Daryl, Grade: 8, Graduated with an average score: 5.95",
  "Student name: Bill, Grade: 9, Graduated with an average score: 6.00",
  "Student name: Philip, Grade: 10, Graduated with an average score: 5.05",
  "Student name: Peter, Grade: 11, Graduated with an average score: 4.88",
  "Student name: Gavin, Grade: 10, Graduated with an average score: 4.00",
]);

school([
  "Student name: George, Grade: 5, Graduated with an average score: 2.75",
  "Student name: Alex, Grade: 9, Graduated with an average score: 3.66",
  "Student name: Peter, Grade: 8, Graduated with an average score: 2.83",
  "Student name: Boby, Grade: 5, Graduated with an average score: 4.20",
  "Student name: John, Grade: 9, Graduated with an average score: 2.90",
  "Student name: Steven, Grade: 2, Graduated with an average score: 4.90",
  "Student name: Darsy, Grade: 1, Graduated with an average score: 5.15",
]);
