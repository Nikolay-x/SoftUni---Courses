function chrInRange(chr1, chr2) {
  let chr1Ascii = chr1.charCodeAt(0);
  let chr2Ascii = chr2.charCodeAt(0);
  if (chr1Ascii <= chr2Ascii) {
    var start = chr1Ascii;
    var end = chr2Ascii;
  } else {
    var start = chr2Ascii;
    var end = chr1Ascii;
  }
  let result = [];
  for (let i = start + 1; i < end; i++) {
    result.push(String.fromCharCode(i));
  }
  return result.join(" ");
}

function charInRange(chr1, chr2) {
  let min = Math.min(chr1.charCodeAt(0), chr2.charCodeAt(0));
  let max = Math.max(chr1.charCodeAt(0), chr2.charCodeAt(0));

  let result = [];
  for (let i = min + 1; i < max; i++) {
    result.push(String.fromCharCode(i));
  }
  return result.join(" ");
}

console.log(chrInRange("a", "d"));
console.log(chrInRange("#", ":"));
console.log(chrInRange("C", "#"));

console.log(charInRange("a", "d"));
console.log(charInRange("#", ":"));
console.log(charInRange("C", "#"));
