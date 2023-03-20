function attachEventsListeners() {
  const inputUnits = document.querySelector("#inputUnits");
  const inputDistance = document.querySelector("#inputDistance");
  const outputUnits = document.querySelector("#outputUnits");
  const outputDistance = document.querySelector("#outputDistance");
  const btnConvert = document.querySelector("#convert");

  btnConvert.addEventListener("click", (x) => {
    const units = {
      km: 1000,
      m: 1,
      cm: 0.01,
      mm: 0.001,
      mi: 1609.34,
      yrd: 0.9144,
      ft: 0.3048,
      in: 0.0254,
    };

    let fromValue = Number(inputDistance.value) * units[inputUnits.value];
    outputDistance.disabled = false;
    outputDistance.value = fromValue / units[outputUnits.value];
  });
}
