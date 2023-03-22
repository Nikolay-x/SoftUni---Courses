function loadRepos() {
  const BASE_URL = "https://api.github.com/users/testnakov/repos";
  const resultContainer = document.getElementById("res");
  const fetchAllRepos = fetch(BASE_URL, { method: "GET" }); // Promise

  fetchAllRepos
    .then((res) => {
      console.log(res.status); // to check the return status
      return res.text();
    })
    .then((data) => {
      resultContainer.textContent = data;
    })
    .catch((err) => {
      console.error.apply(err);
    });
}
