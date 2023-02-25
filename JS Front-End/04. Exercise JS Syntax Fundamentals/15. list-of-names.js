function namesList(names) {
  sortedNamesAsc = [...names].sort((a, b) => {
    let result = a.localeCompare(b);
    return result;
  });
  for (let i = 0; i <= sortedNamesAsc.length - 1; i++) {
    console.log(`${i + 1}.${sortedNamesAsc[i]}`);
  }
}

function listOfNames(names) {
  console.log(
    [...names]
      .sort((aName, bName) => aName.localeCompare(bName))
      .map((name, index) => `${index + 1}.${name}`)
      .join("\n")
  );
}

namesList(["John", "Bob", "Christina", "Ema"]);

listOfNames(["John", "Bob", "Christina", "Ema"]);
