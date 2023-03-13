function softuni(list) {
  courses = {};

  for (const line of list) {
    if (line.includes(":")) {
      let [name, capacity] = line.split(": ");
      if (!courses.hasOwnProperty(name)) {
        courses[name] = {};
        courses[name].capacity = Number(capacity);
        courses[name].students = [];
      } else {
        courses[name].capacity += Number(capacity);
      }
    } else if (line.includes("with email")) {
      let [userCredits, emailCourse] = line.split("] with email ");
      let [user, credits] = userCredits.split("[");
      let [email, courseName] = emailCourse.split(" joins ");
      if (
        courses.hasOwnProperty(courseName) &&
        courses[courseName].capacity >= 1
      ) {
        courses[courseName].students.push([user, email, Number(credits)]);
        courses[courseName].capacity -= 1;
      }
    }
  }

  let sortedCourses = Object.entries(courses).sort(
    (a, b) => b[1].students.length - a[1].students.length
  );

  for (const course of sortedCourses) {
    console.log(`${course[0]}: ${course[1].capacity} places left`);

    let sortedStudents = course[1].students.sort((a, b) => b[2] - a[2]);
    for (const student of sortedStudents) {
      console.log(`--- ${student[2]}: ${student[0]}, ${student[1]}`);
    }
  }
}

softuni([
  "JavaBasics: 2",
  "user1[25] with email user1@user.com joins C#Basics",
  "C#Advanced: 3",
  "JSCore: 4",
  "user2[30] with email user2@user.com joins C#Basics",
  "user13[50] with email user13@user.com joins JSCore",
  "user1[25] with email user1@user.com joins JSCore",
  "user8[18] with email user8@user.com joins C#Advanced",
  "user6[85] with email user6@user.com joins JSCore",
  "JSCore: 2",
  "user11[3] with email user11@user.com joins JavaBasics",
  "user45[105] with email user45@user.com joins JSCore",
  "user007[20] with email user007@user.com joins JSCore",
  "user700[29] with email user700@user.com joins JSCore",
  "user900[88] with email user900@user.com joins JSCore",
]);
