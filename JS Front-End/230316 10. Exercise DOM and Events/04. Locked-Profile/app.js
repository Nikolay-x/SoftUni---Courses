function lockedProfile() {
  const mainDivs = document.querySelectorAll(".profile");

  for (const mainDiv of mainDivs) {
    const unlockRadioInput = mainDiv.children[4];
    const hiddenDiv = mainDiv.children[9];
    const btn = mainDiv.children[10];

    btn.addEventListener("click", eventHandler);

    function eventHandler() {
      if (unlockRadioInput.checked) {
        if (btn.textContent === "Show more") {
          btn.textContent = "Hide it";
          hiddenDiv.style.display = "block";
        } else {
          btn.textContent = "Show more";
          hiddenDiv.style.display = "none";
        }
      }
    }
  }
}

// function lockedProfile() {
//   const buttons = Array.from(document.getElementsByTagName("button"));
//   buttons.forEach((button) => {
//     button.addEventListener("click", toggleInfo);
//   });

//   function toggleInfo(e) {
//     const btn = e.currentTarget;
//     const currentProfile = btn.parentElement;
//     const children = Array.from(currentProfile.children);
//     const unlockRadioInput = children[4];
//     const additionalInfoDiv = children[9];

//     if (unlockRadioInput.checked) {
//       if (btn.textContent === "Show more") {
//         btn.textContent = "Hide it";
//         additionalInfoDiv.style.display = "block";
//       } else {
//         btn.textContent = "Show more";
//         additionalInfoDiv.style.display = "none";
//       }
//     }
//   }
// }
