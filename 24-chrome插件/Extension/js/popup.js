function getUrlList() {
  chrome.runtime.sendMessage({ event: 'openUrl', url: 'https://www.baidu.com' });
}

function getInfo() {
  // chrome.runtime.sendMessage({});
}

document.getElementById('btn1').addEventListener('click', getUrlList);
document.getElementById('btn2').addEventListener('click', getInfo);
