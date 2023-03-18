function create(words) {
  const content = document.getElementById("content");

  for (const word of words) {
    let newDiv = document.createElement("div");
    let newPargraph = document.createElement("p");
    newPargraph.textContent = word;
    newPargraph.style.display = "none";
    newDiv.appendChild(newPargraph);

    //  newDiv.addEventListener("click", () => {
    //    newPargraph.style.display = "block";
    //  });

    newDiv.addEventListener("click", eventHandler);
    content.appendChild(newDiv);

    function eventHandler(event) {
      const div = event.currentTarget;
      const p = div.children[0];
      p.style.display = "block"
    }
  }
}

// //  *** eventHandler to toggle the display ***
// function create(words) {
//   const content = document.getElementById("content");

//   for (const word of words) {
//     let newDiv = document.createElement("div");
//     let newPargraph = document.createElement("p");
//     newPargraph.textContent = word;
//     newPargraph.style.display = "none";
//     newDiv.appendChild(newPargraph);

//     newDiv.addEventListener("click", eventHandler);
//     content.appendChild(newDiv);

//     function eventHandler(event) {
//       const div = event.currentTarget;
//       const p = div.children[0];
//       if (p.style.display === "none") {
//         p.style.display = "block";
//       } else {
//         p.style.display = "none";
//       }
//     }
//   }
// }
