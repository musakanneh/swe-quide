"use strict";

var wordPattern = function wordPattern(pattern, s) {
  var splitString = s.split(' ');
  if (splitString.length !== pattern.length) return false;
  var map = {};

  for (var i = 0; i < pattern.length; i++) {
    var letterFromPattern = pattern[i];
    var wordFromSplitString = splitString[i];

    if (map[letterFromPattern]) {
      if (map[letterFromPattern] !== wordFromSplitString) {
        return false;
      }
    } else {
      if (Object.values(map).includes(wordFromSplitString)) {
        return false;
      }

      map[letterFromPattern] = wordFromSplitString;
    }
  }

  return true;
};

console.log(wordPattern("aaaa", "dog cat cat dog"));