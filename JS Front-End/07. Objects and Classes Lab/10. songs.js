function songsCreator(arr) {
  let songsNumber = arr.shift();
  let typeList = arr.pop();

  class Song {
    constructor(typeList, name, time) {
      this.typeList = typeList;
      this.name = name;
      this.time = time;
    }
  }

  let songs = [];
  for (let i = 0; i < songsNumber; i++) {
    let [typeList, name, time] = arr[i].split("_");
    songs.push(new Song(typeList, name, time));
  }

  for (let song of songs) {
    if (typeList === "all") {
      console.log(song.name);
    } else if (song.typeList === typeList) {
      console.log(song.name);
    }
  }
}

songsCreator([
  3,
  "favourite_DownTown_3:14",
  "favourite_Kiss_4:16",
  "favourite_Smooth Criminal_4:01",
  "favourite",
]);

songsCreator([
  4,
  "favourite_DownTown_3:14",
  "listenLater_Andalouse_3:24",
  "favourite_In To The Night_3:58",
  "favourite_Live It Up_3:48",
  "listenLater",
]);

songsCreator([2, "like_Replay_3:15", "ban_Photoshop_3:48", "all"]);
