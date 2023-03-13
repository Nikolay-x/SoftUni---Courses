function bookShelves(list) {
  let shelves = {};
  for (const line of list) {
    if (line.includes("->")) {
      let [shelfId, shelfGenre] = line.split(" -> ");
      if (!shelves.hasOwnProperty(shelfId)) {
        shelves[shelfId] = {};
        shelves[shelfId].genre = shelfGenre;
        shelves[shelfId].books = [];
      }
    } else if (line.includes(":")) {
      let [bookTitle, bookInfo] = line.split(": ");
      let [bookAuthor, bookGenre] = bookInfo.split(", ");
      let book = {};
      book.title = bookTitle;
      book.author = bookAuthor;
      book.genre = bookGenre;
      for (id in shelves) {
        if (shelves[id].genre === book.genre) {
          shelves[id].books.push(book);
        }
      }
    }
  }

  sortedShelves = Object.entries(shelves).sort(
    (a, b) => b[1].books.length - a[1].books.length
  );

  for (const shelf of sortedShelves) {
    console.log(`${shelf[0]} ${shelf[1].genre}: ${shelf[1].books.length}`);
    let sortedBooks = shelf[1].books.sort((a, b) =>
      a.title.localeCompare(b.title)
    );
    for (const book of sortedBooks) {
      console.log(`--> ${book.title}: ${book.author}`);
    }
  }
}

bookShelves([
  "1 -> history",
  "1 -> action",
  "Death in Time: Criss Bell, mystery",
  "2 -> mystery",
  "3 -> sci-fi",
  "Child of Silver: Bruce Rich, mystery",
  "Hurting Secrets: Dustin Bolt, action",
  "Future of Dawn: Aiden Rose, sci-fi",
  "Lions and Rats: Gabe Roads, history",
  "2 -> romance",
  "Effect of the Void: Shay B, romance",
  "Losing Dreams: Gail Starr, sci-fi",
  "Name of Earth: Jo Bell, sci-fi",
  "Pilots of Stone: Brook Jay, history",
]);

bookShelves([
  "1 -> mystery",
  "2 -> sci-fi",
  "Child of Silver: Bruce Rich, mystery",
  "Lions and Rats: Gabe Roads, history",
  "Effect of the Void: Shay B, romance",
  "Losing Dreams: Gail Starr, sci-fi",
  "Name of Earth: Jo Bell, sci-fi",
]);
