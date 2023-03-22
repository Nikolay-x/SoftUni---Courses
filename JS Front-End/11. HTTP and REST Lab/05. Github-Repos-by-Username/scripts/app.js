function loadRepos() {
  const BASE_URL = "https://api.github.com/users/";
  const username = document.querySelector("#username");
  const list = document.getElementById("repos");

  const usernameVal = username.value;

  fetch(`${BASE_URL}${usernameVal}/repos`, { method: "GET" })
    .then((res) => res.json())
    .then((repos) => {
      //   console.log(usernameVal);
      //   console.log(repos);
      list.textContent = "";
      repos.forEach((repoRes) => {
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.href = `${repoRes.html_url}`;
        a.textContent = `${repoRes.full_name}`;
        li.appendChild(a);
        list.appendChild(li);
      });
    })
    .catch((err) => {
      const li = document.createElement("li");
      li.textContent = err.message;
      list.appendChild(li);
    });
}
