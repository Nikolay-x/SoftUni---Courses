function moviesFunc(inputArr) {
  let movies = [];
  for (const line of inputArr) {
    if (line.includes("addMovie")) {
      let name = line.split("addMovie ")[1];
      let movie = {};
      movie.name = name;
      movies.push(movie);
    } else if (line.includes("directedBy")) {
      let [name, director] = line.split(" directedBy ");
      for (let movie of movies) {
        if (movie.name === name) {
          movie.director = director;
        }
      }
    } else if (line.includes("onDate")) {
      let [name, date] = line.split(" onDate ");
      for (let movie of movies) {
        if (movie.name === name) {
          movie.date = date;
        }
      }
    }
  }
  for (let movie of movies) {
    if (movie.name && movie.director && movie.date) {
      console.log(JSON.stringify(movie));
    }
  }
}

function moviesFuncDemo(inputArr) {
  let movies = [];
  for (const line of inputArr) {
    let commandTokens = line.split(" ");
    if (line.includes("addMovie")) {
      let name = commandTokens.slice(1).join(" ");
      addMovie(name);
    } else if (line.includes("directedBy")) {
      let indexOfCommand = commandTokens.indexOf("directedBy");
      let name = commandTokens.slice(0, indexOfCommand).join(" ");
      let director = commandTokens.slice(indexOfCommand + 1).join(" ");
      addDirector(name, director);
    } else if (line.includes("onDate")) {
      let indexOfCommand = commandTokens.indexOf("onDate");
      let name = commandTokens.slice(0, indexOfCommand).join(" ");
      let date = commandTokens.slice(indexOfCommand + 1).join(" ");
      addDate(name, date);
    }
  }
  //   for (let movie of movies) {
  //     if (
  //       movie.hasOwnProperty("name") &&
  //       movie.hasOwnProperty("director") &&
  //       movie.hasOwnProperty("date")
  //     ) {
  //       console.log(JSON.stringify(movie));
  //     }
  //   }

  let filteredMovies = movies.filter(
    (m) =>
      m.hasOwnProperty("name") &&
      m.hasOwnProperty("director") &&
      m.hasOwnProperty("date")
  );
  for (let movie of filteredMovies) {
    console.log(JSON.stringify(movie));
  }

  function addMovie(name) {
    movies.push({ name });
  }

  function addDirector(name, director) {
    let movie = movies.find((m) => m.name === name);
    if (movie) {
      movie.director = director;
    }
  }

  function addDate(name, date) {
    let movie = movies.find((m) => m.name === name);
    if (movie) {
      movie.date = date;
    }
  }
}

moviesFunc([
  "addMovie Fast and Furious",
  "addMovie Godfather",
  "Inception directedBy Christopher Nolan",
  "Godfather directedBy Francis Ford Coppola",
  "Godfather onDate 29.07.2018",
  "Fast and Furious onDate 30.07.2018",
  "Batman onDate 01.08.2018",
  "Fast and Furious directedBy Rob Cohen",
]);

moviesFunc([
  "addMovie The Avengers",
  "addMovie Superman",
  "The Avengers directedBy Anthony Russo",
  "The Avengers onDate 30.07.2010",
  "Captain America onDate 30.07.2010",
  "Captain America directedBy Joe Russo",
]);

moviesFuncDemo([
  "addMovie Fast and Furious",
  "addMovie Godfather",
  "Inception directedBy Christopher Nolan",
  "Godfather directedBy Francis Ford Coppola",
  "Godfather onDate 29.07.2018",
  "Fast and Furious onDate 30.07.2018",
  "Batman onDate 01.08.2018",
  "Fast and Furious directedBy Rob Cohen",
]);

moviesFuncDemo([
  "addMovie The Avengers",
  "addMovie Superman",
  "The Avengers directedBy Anthony Russo",
  "The Avengers onDate 30.07.2010",
  "Captain America onDate 30.07.2010",
  "Captain America directedBy Joe Russo",
]);
