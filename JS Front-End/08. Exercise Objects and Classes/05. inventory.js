function herosFunc(inputArr) {
  let heros = [];
  for (let line of inputArr) {
    let [name, level, items] = line.split(" / ");
    let hero = { name, level, items };
    heros.push(hero);
  }

  heros
    .sort((heroA, heroB) => heroA.level - heroB.level)
    .forEach((h) => {
      console.log(`Hero: ${h.name}`);
      console.log(`level => ${h.level}`);
      console.log(`items => ${h.items}`);
    });
}

herosFunc([
  "Isacc / 25 / Apple, GravityGun",
  "Derek / 12 / BarrelVest, DestructionSword",
  "Hes / 1 / Desolator, Sentinel, Antara",
]);
