chrome.action.onClicked.addListener((tab) => {
    chrome.scripting.executeScript({
      target: {tabId: tab.id},
      files: ['dist/bundle.js']  // Your bundled script that includes the tokenizer and model inference logic
    });
  });
  