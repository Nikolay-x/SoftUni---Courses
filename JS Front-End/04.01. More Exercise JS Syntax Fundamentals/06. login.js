function login(arr) {
  let username = arr[0];
  let passwords = arr.slice(1);
  let password = username.split("").reverse().join("");
  let count = 0;
  for (const pass of passwords) {
    if (pass === password) {
      console.log(`User ${username} logged in.`);
      break;
    } else {
      count++;
      if (count < 4) {
        console.log("Incorrect password. Try again.");
      } else {
        console.log(`User ${username} blocked!`);
        break;
      }
    }
  }
}

login(["Acer", "login", "go", "let me in", "recA"]);
login(["momo", "omom"]);
login(["sunny", "rainy", "cloudy", "sunny", "not sunny"]);
