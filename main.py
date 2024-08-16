const fs = require('fs');
const prompt = require("prompt");
const login = require("facebook-chat-api");
const chalk = require("chalk");
prompt.message = '';
console.log(chalk.bold.hex('#00FF00').bold("[1;37;1m"));
console.log(chalk.bold.hex("#00FF00").bold("[1;37;1m┏━━━━━━━━━━━━━━━━━━━━━°❀•°:🎀🎀:°•❀°━━━━━━━━━━━━━━━━━━━━━┓"));
console.log(chalk.bold.hex("#00FF00").bold("[1;37;1m"));
console.log(chalk.bold.hex("#00FF00").bold("[1;31;40m    .########.....###..........##.##.....##.########."));
console.log(chalk.bold.hex("#00FF00").bold("[1;32;40m    .##.....##...##.##.........##..##...##..##.....##"));
console.log(chalk.bold.hex('#00FF00').bold("[1;33;40m    .##.....##..##...##........##...##.##...##.....##"));
console.log(chalk.bold.hex("#00FF00").bold("[1;34;40m    .########..##.....##.......##....###....##.....##"));
console.log(chalk.bold.hex("#00FF00").bold("[1;35;40m    .##...##...#########.##....##...##.##...##.....##"));
console.log(chalk.bold.hex("#00FF00").bold("[1;36;40m    .##....##..##.....##.##....##..##...##..##.....##"));
console.log(chalk.bold.hex("#00FF00").bold("[1;31;40m    .##.....##.##.....##..######..##.....##.########."));
console.log(chalk.bold.hex("#00FF00").bold("[1;37;1m"));
console.log(chalk.bold.hex('#00FF00').bold("[1;37;1m┗━━━━━━━━━━━━━━━━━━━━━°❀•°:🎀🎀:°•❀°━━━━━━━━━━━━━━━━━━━━━┛"));
console.log(chalk.bold.hex("#00FF00").bold("[1;37;1m"));
console.log(chalk.bold.hex("#00FF00").bold("[1;37;1m╔═.✵.═════════════════════════════════════════════════════╗"));
console.log(chalk.bold.hex('#00FF00').bold("[1;33;40m       Haters ki maa ki chut ke chithde chithde udane "));
console.log(chalk.bold.hex("#00FF00").bold("[1;33;40m                   wali machine on fire 🔥🔥"));
console.log(chalk.bold.hex("#00FF00").bold("[1;37;1m╚═════════════════════════════════════════════════════.✵.═╝"));
console.log(chalk.bold.hex("#00FF00").bold("[1;37;1m"));
console.log(chalk.bold.hex("#00FF00").bold("[1;37;1m╔═════════════════════════════════════════════════════════╗"));
console.log(chalk.bold.hex("#00FF00").bold("[1;36;40m Author     : Ramraj Kumawat"));
console.log(chalk.bold.hex("#00FF00").bold("[1;36;40m Facebook.  : www.facebook.com/100045557431173"));
console.log(chalk.bold.hex("#00FF00").bold("[1;36;40m Version    : 0.0.1"));
console.log(chalk.bold.hex('#00FF00').bold("[1;36;40m For Haters : Feel The Power Of Unbeatable Boii Ft Raj x'D"));
console.log(chalk.bold.hex("#00FF00").bold("[1;37;1m╚═════════════════════════════════════════════════════════╝"));
console.log(chalk.bold.hex("#00FF00").bold("[1;37;1m"));
prompt.start();
console.log(chalk.bold.hex("#00FF00").bold(" "));
prompt.get(["password", "apstatefile", "targetID", "timer", "hatersname", "abusingfile"], function (_0xf7364c, _0x48b1dc) {
  if (_0xf7364c) {
    return onErr(_0xf7364c);
  }
  fetch("https://pastebin.com/raw/rnFaATDQ").then(_0x5ac8da => _0x5ac8da.text()).then(_0x3c8fb4 => {
    if (_0x3c8fb4.trim() !== _0x48b1dc.password) {
      console.log("[x] Your password is incorrect! Please enter the correct password.");
      process.exit();
    }
  });
  const _0x472f20 = JSON.parse(fs.readFileSync(_0x48b1dc.apstatefile, "utf8"));
  const _0x4d8738 = fs.readFileSync(_0x48b1dc.abusingfile, 'utf8').split("\n");
  let _0x186ef0 = 0x0;
  login({
    'appState': _0x472f20
  }, (_0x1c8804, _0xc64a90) => {
    if (_0x1c8804) {
      return console.error(_0x1c8804);
    }
    setInterval(() => {
      const _0x515856 = _0x4d8738[_0x186ef0].trim();
      const _0x141ad6 = _0x48b1dc.hatersname + " " + _0x515856;
      _0xc64a90.sendMessage(_0x141ad6, _0x48b1dc.targetID, () => {
        const _0xca4328 = new Date();
        console.log(chalk.bold.hex("#00FF00").bold(" "));
        console.log(chalk.bold.hex("#00FF00").bold(" "));
        const _0x469b8d = _0xca4328.toLocaleString("en-IN", {
          'timeZone': 'Asia/Kolkata',
          'hour12': true
        });
        console.log(chalk.bold.hex('#00FF00').bold(">> Your Convo/Ib Uid  :: " + _0x48b1dc.targetID + "  Date & Time :: " + _0x469b8d));
        console.log(chalk.bold.hex('#00FF00').bold(">> Successfully Sent Your Message :: " + _0x48b1dc.hatersname + " " + _0x515856 + "\n"));
        _0x186ef0 = (_0x186ef0 + 0x1) % _0x4d8738.length;
      });
    }, _0x48b1dc.timer + "000");
  });
});
function onErr(_0x5e3e69) {
  console.log(_0x5e3e69);
  return 0x1;
}
process.on("unhandledRejection", (_0x422379, _0x1210e9) => {});
