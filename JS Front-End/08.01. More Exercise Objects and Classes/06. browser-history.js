function browserHistory(state, commands) {
  for (const command of commands) {
    if (command === "Clear History and Cache") {
      state["Open Tabs"].splice(0);
      state["Recently Closed"].splice(0);
      state["Browser Logs"].splice(0);
    } else {
      let [action, tab] = command.split(" ");
      if (action === "Open") {
        state["Open Tabs"].push(tab);
        state["Browser Logs"].push(command);
      } else if (action === "Close") {
        if (state["Open Tabs"].includes(tab)) {
          let index = state["Open Tabs"].indexOf(tab);
          state["Open Tabs"].splice(index, 1);
          state["Recently Closed"].push(tab);
          state["Browser Logs"].push(command);
        }
      }
    }
  }

  console.log(state["Browser Name"]);
  console.log(`Open Tabs: ${state["Open Tabs"].join(", ")}`);
  console.log(`Recently Closed: ${state["Recently Closed"].join(", ")}`);
  console.log(`Browser Logs: ${state["Browser Logs"].join(", ")}`);
}

browserHistory(
  {
    "Browser Name": "Google Chrome",
    "Open Tabs": ["Facebook", "YouTube", "Google Translate"],
    "Recently Closed": ["Yahoo", "Gmail"],
    "Browser Logs": [
      "Open YouTube",
      "Open Yahoo",
      "Open Google Translate",
      "Close Yahoo",
      "Open Gmail",
      "Close Gmail",
      "Open Facebook",
    ],
  },
  ["Close Facebook", "Open StackOverFlow", "Open Google"]
);

browserHistory(
  {
    "Browser Name": "Mozilla Firefox",
    "Open Tabs": ["YouTube"],
    "Recently Closed": ["Gmail", "Dropbox"],
    "Browser Logs": [
      "Open Gmail",
      "Close Gmail",
      "Open Dropbox",
      "Open YouTube",
      "Close Dropbox",
    ],
  },
  ["Open Wikipedia", "Clear History and Cache", "Open Twitter"]
);
