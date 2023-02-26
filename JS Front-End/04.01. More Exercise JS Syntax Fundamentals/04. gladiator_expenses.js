function gladiatorExp(lostFights, helmet, sword, shield, armor) {
  let expenses = 0;
  let shieldCount = 0;
  for (let i = 1; i <= lostFights; i++) {
    if (i % 2 === 0) {
      expenses += helmet;
    }
    if (i % 3 === 0) {
      expenses += sword;
    }
    if (i % 6 === 0) {
      expenses += shield;
      shieldCount += 1;
      if (shieldCount % 2 === 0) {
        expenses += armor;
      }
    }
  }
  console.log(`Gladiator expenses: ${expenses.toFixed(2)} aureus`);
}

gladiatorExp(7, 2, 3, 4, 5);
gladiatorExp(23, 12.5, 21.5, 40, 200);
