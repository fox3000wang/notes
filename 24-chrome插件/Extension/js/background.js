// background.js 常驻在后台，生命周期相对长
console.log('background.js');

// TODO: 通信的借口需要统一设计
function openUrl(request, sender, sendResponse) {
  if (request.event === 'openUrl') {
    chrome.tabs.create({ url: request.url });
  }
}
chrome.runtime.onMessage.addListener(openUrl);
