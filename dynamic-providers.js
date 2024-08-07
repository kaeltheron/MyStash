

// 获取前一天的日期
const date = new Date();
date.setDate(date.getDate() - 1);

const year = date.getFullYear();
const month = (`0${date.getMonth() + 1}`).slice(-2); // 补零
const day = (`0${date.getDate()}`).slice(-2); // 补零
const fullDate = `${year}${month}${day}`;

const overrideContent = `
proxy-providers:
  dynamic-provider:
    url: https://nodefree.githubrowcontent.com/${year}/${month}/${fullDate}.yaml
    interval: 3600`;
console.log(overrideContent);
$done({
  overrideContent
})
