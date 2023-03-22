function loadCommits() {
  // Try it with Fetch API
  const BASE_URL = "https://api.github.com/repos/";
  const username = document.getElementById("username");
  const repo = document.getElementById("repo");
  const commits = document.getElementById("commits");

  const usernameVal = username.value;
  const repoVal = repo.value;

  fetch(`${BASE_URL}${usernameVal}/${repoVal}/commits`, { method: "GET" })
    .then((res) => res.json())
    // .then((data) => {
    //   //   console.log(data);
    //   data.forEach((commitRes) => {
    //     const li = document.createElement("li");
    //     li.textContent = `${commitRes.commit.author.name}: ${commitRes.commit.message}`;
    //     commits.appendChild(li);
    //   });
    // })
    .then((data) => {
      data.forEach(({ commit }) => {
        const li = document.createElement("li");
        li.textContent = `${commit.author.name}: ${commit.message}`;
        commits.appendChild(li);
      });
    })
    .catch((err) => {
      const li = document.createElement("li");
      li.textContent = err.message;
      commits.appendChild(li);
    });
}
