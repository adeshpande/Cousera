#!/usr/bin/env node

var prime = function (n) {
    if (n === 2 || n === 3 || n === 5 || n === 7 || n === 11 || n === 13 || n === 17 || n === 19) {return n;}
    if (n % 2 > 0 && n % 3 > 0 && n % 5 > 0 && n % 7 > 0 && n % 11 > 0 && n % 13 > 0 && n % 17 > 0 && n % 19 > 0 && n % Math.sqrt (n) > 0) {return n;}
};

var first100primes = function(k) {
    var n = 1;
    var arr = [];

    for (n = 1; n < k+1; n++) {
        arr.push(prime (n));
    }
    arr = arr.filter(Number);
    arr.length=100;
    return arr;
};

var fmt = function (arr) {
    return arr;
};

var final = (fmt(first100primes(1000)));

var fs = require(‘fs’);
var outfile = “prime.txt”;
var out = final + “,”;
fs.writeFileSync(outfile, out);
console.log(“Script: ” + __filename + “\nWrote: ” + out + “To: ” + outfile);
