function vacation(groupSize, groupType, day) {
  let totalPrice;
  if (groupType === "Students") {
    if (day === "Friday") {
      totalPrice = groupSize * 8.45;
    } else if (day === "Saturday") {
      totalPrice = groupSize * 9.8;
    } else if (day === "Sunday") {
      totalPrice = groupSize * 10.46;
    }
    if (groupSize >= 30) {
      totalPrice -= totalPrice * 0.15;
    }
  } else if (groupType === "Business") {
    if (groupSize >= 100) {
      groupSize -= 10;
    }
    if (day === "Friday") {
      totalPrice = groupSize * 10.9;
    } else if (day === "Saturday") {
      totalPrice = groupSize * 15.6;
    } else if (day === "Sunday") {
      totalPrice = groupSize * 16;
    }
  } else if (groupType === "Regular") {
    if (day === "Friday") {
      totalPrice = groupSize * 15;
    } else if (day === "Saturday") {
      totalPrice = groupSize * 20;
    } else if (day === "Sunday") {
      totalPrice = groupSize * 22.5;
    }
    if (10 <= groupSize && groupSize <= 20) {
      totalPrice -= totalPrice * 0.05;
    }
  }
  console.log(`Total price: ${totalPrice.toFixed(2)}`);
}

vacation(30, "Students", "Sunday");
vacation(100, "Business", "Sunday");
vacation(40, "Regular", "Saturday");
