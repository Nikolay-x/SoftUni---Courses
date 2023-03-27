function attachEvents() {
  const btnLoadPosts = document.querySelector("#btnLoadPosts");
  const btnViewPost = document.getElementById("btnViewPost");
  const postsTitle = document.getElementById("posts");
  const postTitle = document.getElementById("post-title");
  const postBody = document.getElementById("post-body");
  const postComments = document.getElementById("post-comments");
  const BASE_URL_POSTS = "http://localhost:3030/jsonstore/blog/posts";
  const BASE_URL_COMMENTS = "http://localhost:3030/jsonstore/blog/comments";

  let allPosts = {};

  btnLoadPosts.addEventListener("click", loadPostshandler);
  btnViewPost.addEventListener("click", viewPostHandler);

  async function loadPostshandler() {
    const posts = await fetch(BASE_URL_POSTS);
    const postsData = await posts.json();
    allPosts = postsData;
    for (key in postsData) {
      let { body, id, title } = postsData[key];
      createElement("option", title, postsTitle, "", [], { value: id });
    }
  }

  async function viewPostHandler() {
    const comments = await fetch(BASE_URL_COMMENTS);
    const commentsData = await comments.json();

    postComments.innerHTML = "";
    postTitle.textContent = "";
    postBody.textContent = "";

    let selectedOption = postsTitle.options[postsTitle.selectedIndex];
    const chosenPost = selectedOption.textContent;

    for (let postID in allPosts) {
      let { body, id, title } = allPosts[postID];
      if (title === chosenPost) {
        for (let key in commentsData) {
          let { id, postId, text } = commentsData[key];
          if (postID === postId) {
            postTitle.textContent = title;
            postBody.textContent = body;
            createElement("li", text, postComments);
          }
        }
      }
    }
  }

  // type = string
  // content = string (text content)
  // id = string
  // classes = array of strings
  // attributes = object
  function createElement(type, content, parentNode, id, classes, attributes) {
    const htmlElement = document.createElement(type);

    if (content && type !== "input" && type !== "textarea") {
      // if (content && type !== "input") {
      htmlElement.textContent = content;
    }

    if (content && type === "input") {
      htmlElement.value = content;
    }

    if (content && type === "textarea") {
      htmlElement.value = content;
    }

    if (id) {
      htmlElement.id = id;
    }

    // ["list", "item"]
    if (classes) {
      htmlElement.classList.add(...classes);
    }

    // { src: "link to image", href: "link to site", type: "checkbox" ... }
    if (attributes) {
      for (const key in attributes) {
        htmlElement.setAttribute(key, attributes[key]);
      }
    }

    if (parentNode) {
      parentNode.appendChild(htmlElement);
    }

    return htmlElement;
  }
}

attachEvents();
