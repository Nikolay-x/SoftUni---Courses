function attachGradientEvents() {
  const gradient = document.querySelector("#gradient");
  const result = document.querySelector("#result");

  gradient.addEventListener("mousemove", mousemoveHandler);
  gradient.addEventListener("mouseout", mouseoutHandler);

  function mousemoveHandler(event) {
    const x = event.offsetX;
    const width = gradient.clientWidth;
    const percentage = parseInt((x / width) * 100); // show from 0 to 99 %
    result.textContent = `${percentage}%`;
  }

  function mouseoutHandler() {
    result.textContent = "";
  }
}

// function attachGradientEvents() {
//     const gradient = document.querySelector("#gradient");
//     const result = document.querySelector("#result");
  
//     gradient.addEventListener("mousemove", mousemoveHandler);
//     gradient.addEventListener("mouseout", mouseoutHandler);
  
//     function mousemoveHandler(event) {
//       const x = event.offsetX;
//       const width = gradient.clientWidth;
//       const percentage = Math.ceil(Number((x / width) * 100)); // show from 0 to 100%
//       result.textContent = `${percentage}%`;
//     }
  
//     function mouseoutHandler() {
//       result.textContent = "";
//     }
//   }
