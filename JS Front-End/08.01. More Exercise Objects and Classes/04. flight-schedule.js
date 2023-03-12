function flightScheduler(inputArr) {
  let flights = {};
  for (const line of inputArr[0]) {
    let [flightNumber, ...destination] = line.split(" ");
    flights[flightNumber] = {};
    flights[flightNumber].Destination = destination.join(" ");
    flights[flightNumber].Status = "";
  }

  for (const line of inputArr[1]) {
    let [flightNumber, statusCur] = line.split(" ");
    if (flights.hasOwnProperty(flightNumber)) {
      flights[flightNumber].Status = statusCur;
    }
  }

  let statusFlights = inputArr[2][0];

  for (const flight of Object.entries(flights)) {
    if (flight[1].Status.length === 0 && statusFlights === "Ready to fly") {
      flight[1].Status = "Ready to fly";
    }
    if (flight[1].Status === statusFlights) {
      console.log(flight[1]);
    }
  }
}

// flightScheduler([
//   [
//     "WN269 Delaware",
//     "FL2269 Oregon",
//     "WN498 Las Vegas",
//     "WN3145 Ohio",
//     "WN612 Alabama",
//     "WN4010 New York",
//     "WN1173 California",
//     "DL2120 Texas",
//     "KL5744 Illinois",
//     "WN678 Pennsylvania",
//   ],
//   [
//     "DL2120 Cancelled",
//     "WN612 Cancelled",
//     "WN1173 Cancelled",
//     "SK430 Cancelled",
//   ],
//   ["Cancelled"],
// ]);

flightScheduler([
  [
    "WN269 Delaware",
    "FL2269 Oregon",
    "WN498 Las Vegas",
    "WN3145 Ohio",
    "WN612 Alabama",
    "WN4010 New York",
    "WN1173 California",
    "DL2120 Texas",
    "KL5744 Illinois",
    "WN678 Pennsylvania",
  ],
  [
    "DL2120 Cancelled",
    "WN612 Cancelled",
    "WN1173 Cancelled",
    "SK330 Cancelled",
  ],
  ["Ready to fly"],
]);
