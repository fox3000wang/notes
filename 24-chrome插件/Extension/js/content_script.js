console.log('inject load');

async function main() {
  await sleep(2000);
  window.close();
}

// 模拟sleep()
const sleep = delay => new Promise(resolve => setTimeout(resolve, delay));

main();
