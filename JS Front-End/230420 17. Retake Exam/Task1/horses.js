function horsesFunc(input) {
  let horses = input.shift().split("|");
  //   console.log(horses);
  let commandParser = {
    Retake: retake,
    Trouble: trouble,
    Rage: rage,
    Miracle: miracle,
  };

  for (const line of input) {
    if (line === "Finish") {
      break;
    }

    let commandTokens = line.split(" ");
    let command = commandTokens[0];
    commandParser[command](...commandTokens.slice(1));
  }

  console.log(horses.join("->"));
  console.log(`The winner is: ${horses[horses.length - 1]}`);

  function retake(overtakingHorse, overtakenHorse) {
    let leftHorseIndex = horses.indexOf(overtakingHorse);
    let rightHorseIndex = horses.indexOf(overtakenHorse);

    if (leftHorseIndex < rightHorseIndex) {
      horses[leftHorseIndex] = overtakenHorse;
      horses[rightHorseIndex] = overtakingHorse;

      console.log(`${overtakingHorse} retakes ${overtakenHorse}.`);
    }
  }

  function trouble(horseName) {
    let troubleHorseIndex = horses.indexOf(horseName);

    if (troubleHorseIndex > 0) {
      horses.splice(troubleHorseIndex, 1);
      horses.splice(troubleHorseIndex - 1, 0, horseName);
      console.log(`Trouble for ${horseName} - drops one position.`);
    }
  }

  function rage(horseName) {
    let rageHorseIndex = horses.indexOf(horseName);

    if (rageHorseIndex === horses.length - 2) {
      horses.splice(rageHorseIndex, 1);
      horses.push(horseName);
    } else if (rageHorseIndex < horses.length - 2) {
      horses.splice(rageHorseIndex, 1);
      horses.splice(rageHorseIndex + 2, 0, horseName);
    }

    console.log(`${horseName} rages 2 positions ahead.`);
  }

  function miracle() {
    let lastHorse = horses[0];
    horses.splice(0, 1);
    horses.push(lastHorse);
    console.log(`What a miracle - ${lastHorse} becomes first.`);
  }
}

horsesFunc([
  "Bella|Alexia|Sugar",
  "Retake Alexia Sugar",
  "Rage Bella",
  "Trouble Bella",
  "Finish",
]);

horsesFunc([
  "Onyx|Domino|Sugar|Fiona",
  "Trouble Onyx",
  "Retake Onyx Sugar",
  "Rage Domino",
  "Miracle",
  "Finish",
]);

horsesFunc([
  "Fancy|Lilly",
  "Retake Lilly Fancy",
  "Trouble Lilly",
  "Trouble Lilly",
  "Finish",
  "Rage Lilly",
]);
