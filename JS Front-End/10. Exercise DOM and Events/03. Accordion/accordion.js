function toggle() {
  const btn = document.querySelector(".button");
  const hiddenDiv = document.getElementById("extra");

  if (btn.textContent === "More") {
    btn.textContent = "Less";
    hiddenDiv.style.display = "block";
  } else {
    btn.textContent = "More";
    hiddenDiv.style.display = "none";
  }
}

// function toggle() {
//   const extra = document.querySelector("#extra");
//   const button = document.querySelector(".button");

//   if (extra.style.display === "none" || extra.style.display === "") {
//     extra.style.display = "block";
//     button.textContent = "Less";
//   } else {
//     extra.style.display = "none";
//     button.textContent = "More";
//   }
// }
