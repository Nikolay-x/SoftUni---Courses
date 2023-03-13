function commentsList(list) {
  let output = {
    users: [],
    articles: [],
    comments: {},
  };

  for (const line of list) {
    if (line.includes("user")) {
      let userName = line.split("user ")[1];
      if (!output.users.includes(userName)) {
        output.users.push(userName);
      }
    } else if (line.includes("article")) {
      let articleName = line.split("article ")[1];
      if (!output.articles.includes(articleName)) {
        output.articles.push(articleName);
      }
    } else {
      let [userArticle, commentData] = line.split(": ");
      let [userName, articleName] = userArticle.split(" posts on ");
      let [commentTitle, commentContent] = commentData.split(", ");

      if (
        output.users.includes(userName) &&
        output.articles.includes(articleName)
      ) {
        if (!output.comments.hasOwnProperty(articleName)) {
          output.comments[articleName] = {};
          output.comments[articleName].userComments = [];
        }
        output.comments[articleName].userComments.push({
          userName: userName,
          title: commentTitle,
          comment: commentContent,
        });
      }
    }
  }

  let sortedArticles = output.articles.sort((a, b) => {
    let aComments = output.comments[a].userComments.length;
    let bComments = output.comments[b].userComments.length;
    return bComments - aComments;
  });

  sortedArticles.forEach((article) => {
    let comments = output.comments[article].userComments;
    if (comments.length) {
      console.log(`Comments on ${article}`);
      comments
        .sort((a, b) => a.userName.localeCompare(b.userName))
        .forEach((comment) => {
          console.log(
            `--- From user ${comment.userName}: ${comment.title} - ${comment.comment}`
          );
        });
    }
  });
}

commentsList([
  "user aUser123",
  "someUser posts on someArticle: NoTitle, stupidComment",
  "article Books",
  "article Movies",
  "article Shopping",
  "user someUser",
  "user uSeR4",
  "user lastUser",
  "uSeR4 posts on Books: I like books, I do really like them",
  "uSeR4 posts on Movies: I also like movies, I really do",
  "someUser posts on Shopping: title, I go shopping every day",
  "someUser posts on Movies: Like, I also like movies very much",
]);
