function towns(input) {
  let townsArr = [];
  for (let line of input) {
    let [town, latitudeStr, longitudeStr] = line.split(" | ");
    let townObj = {
      town,
      latitude: Number(latitudeStr).toFixed(2),
      longitude: Number(longitudeStr).toFixed(2),
    };
    townsArr.push(townObj);
  }
  for (let town of townsArr) {
    console.log(town);
  }
}

towns(["Sofia | 42.696552 | 23.32601", "Beijing | 39.913818 | 116.363625"]);
