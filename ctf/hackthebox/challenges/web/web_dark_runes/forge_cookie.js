const crypto = require("crypto");

const signString = (s) =>
  crypto
    .createHash("sha256")
    .update(s + SECRET)
    .digest("hex");

const generateCookie = (username, id) => {
  const stringifiedUser = btoa(JSON.stringify({ username, id }));
  const sig = signString(stringifiedUser);
  return `${stringifiedUser}-${sig}`;
};

const cookie = generateCookie("k00lbeanz", 1);
console.log(cookie);