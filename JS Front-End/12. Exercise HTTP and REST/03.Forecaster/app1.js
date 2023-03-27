function attachEvents() {
  const locationNameInput = document.getElementById("location");
  const submitBtn = document.getElementById("submit");
  const divWrapper = document.getElementById("forecast");
  const currentWeatherDiv = document.getElementById("current");
  const upcomingWeatherDiv = document.getElementById("upcoming");
  const LOCATIONS_BASE_URL =
    "http://localhost:3030/jsonstore/forecaster/locations";
  const TODAY_BASE_URL = "http://localhost:3030/jsonstore/forecaster/today/";
  const UPCOMING_BASE_URL =
    "http://localhost:3030/jsonstore/forecaster/upcoming/";

  let locations = {};
  let icons = {
    Sunny: "&#x2600",
    "Partly sunny": "&#x26C5",
    Overcast: "&#x2601",
    Rain: "&#x2614",
    Degrees: "&#176",
  };

  submitBtn.addEventListener("click", submitEventHandler);

  async function submitEventHandler() {
    try {
      let locationName = locationNameInput.value;
      const locations = await fetch(LOCATIONS_BASE_URL);
      const locationsData = await locations.json();

      currentWeatherDiv.children[0].textContent = "Current conditions";
      if (currentWeatherDiv.children[1]) {
        currentWeatherDiv.children[1].style.display = "block";
      }
      upcomingWeatherDiv.style.display = "block";

      let currentCode = "";
      for (line of locationsData) {
        let { code, name } = line;
        if (name === locationName) {
          currentCode = code;
        }
      }

      const currentWR = await fetch(TODAY_BASE_URL + currentCode);
      const currentWeatherData = await currentWR.json();

      // console.log(upcomingWeatherData);

      let { forecast, name } = currentWeatherData;
      let { condition, high, low } = forecast;

      divWrapper.style.display = "block";
      const forcastsDiv = createElement("div", "", currentWeatherDiv, "", [
        "forecasts",
      ]);
      const symbolSpan = createElement("span", "", forcastsDiv, "", [
        "condition",
        "symbol",
      ]);
      symbolSpan.innerHTML = `${icons[condition]}`;
      const conditionSpan = createElement("span", "", forcastsDiv, "", [
        "condition",
      ]);
      const nameSpan = createElement("span", name, conditionSpan, "", [
        "forecast-data",
      ]);
      const lowHighSpan = createElement(
        "span",
        `${low}°/${high}°`,
        conditionSpan,
        "",
        ["forecast-data"]
      );
      const weatherConditionSpan = createElement(
        "span",
        condition,
        conditionSpan,
        "",
        ["forecast-data"]
      );

      const upcomingWR = await fetch(UPCOMING_BASE_URL + currentCode);
      const upcomingWeatherData = await upcomingWR.json();
      // console.log(upcomingWeatherData);

      let upForecast = upcomingWeatherData["forecast"];
      const uForcastsDiv = createElement("div", "", upcomingWeatherDiv, "", [
        "forecast-info",
      ]);
      for (day of upForecast) {
        let { condition, high, low } = day;
        const wrapperSpan = createElement("span", "", uForcastsDiv, "", [
          "upcoming",
        ]);
        const symbolSpan = createElement("span", "", wrapperSpan, "", [
          "symbol",
        ]);
        symbolSpan.innerHTML = `${icons[condition]}`;
        createElement("span", `${low}°/${high}°`, wrapperSpan, "", [
          "forecast-data",
        ]);
        createElement("span", condition, wrapperSpan, "", ["forecast-data"]);
      }
    } catch (error) {
      divWrapper.style.display = "block";
      currentWeatherDiv.children[0].textContent = "Error";
      if (currentWeatherDiv.children[1]) {
        currentWeatherDiv.children[1].style.display = "none";
      }
      upcomingWeatherDiv.style.display = "none";
    }

    locationNameInput.value = "";
    uForcastsDiv.parentNode.removeChild(uForcastsDiv.parentNode.children[1]);
  }

  // type = string
  // content = string (text content)
  // id = string
  // classes = array of strings
  // attributes = object
  function createElement(type, content, parentNode, id, classes, attributes) {
    const htmlElement = document.createElement(type);

    if (content && type !== "input" && type !== "textarea") {
      // if (content && type !== "input") {
      htmlElement.textContent = content;
    }

    if (content && type === "input") {
      htmlElement.value = content;
    }

    if (content && type === "textarea") {
      htmlElement.value = content;
    }

    if (id) {
      htmlElement.id = id;
    }

    // ["list", "item"]
    if (classes) {
      htmlElement.classList.add(...classes);
    }

    // { src: "link to image", href: "link to site", type: "checkbox" ... }
    if (attributes) {
      for (const key in attributes) {
        htmlElement.setAttribute(key, attributes[key]);
      }
    }

    if (parentNode) {
      parentNode.appendChild(htmlElement);
    }

    return htmlElement;
  }
}

attachEvents();
