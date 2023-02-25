function roadRadar(speed, area) {
  let allowedSpeed = 0;
  switch (area) {
    case "motorway":
      allowedSpeed = 130;
      break;
    case "interstate":
      allowedSpeed = 90;
      break;
    case "city":
      allowedSpeed = 50;
      break;
    case "residential":
      allowedSpeed = 20;
      break;
  }
  if (speed <= allowedSpeed) {
    console.log(`Driving ${speed} km/h in a ${allowedSpeed} zone`);
  } else {
    let difference = speed - allowedSpeed;
    let status = "";
    if (0 < difference && difference <= 20) {
      status = "speeding";
    } else if (21 <= difference && difference <= 40) {
      status = "excessive speeding";
    } else {
      status = "reckless driving";
    }
    console.log(
      `The speed is ${difference} km/h faster than the allowed speed of ${allowedSpeed} - ${status}`
    );
  }
}

roadRadar(40, "city");
roadRadar(21, "residential");
roadRadar(120, "interstate");
roadRadar(200, "motorway");
