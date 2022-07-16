"use strict";

var toLowerCase = function toLowerCase(inputString) {
  var letterCount = 0;

  while (letterCount < inputString.length) {
    if (inputString) {
      return inputString.toLowerCase();
    }

    ;
  }

  ;
  letterCount++;
}; // console.log(toLowerCase("MusaKanneh"));


var uniqueInOrder = function uniqueInOrder(iterable) {
  var resArray = [];

  for (var i = 0; i < iterable.length; i++) {
    if (iterable[i] !== iterable[i + 1]) {
      resArray.push(iterable[i]);
    }

    continue;
  }

  return resArray;
}; // console.log(uniqueInOrder('AAAABBBCCDAABBB'));


var capitalizeTitle = function capitalizeTitle(title) {
  var resultArray = [];
  var splitTitle = title.split(' ');

  for (var i = 0; i < splitTitle.length; i++) {
    var charCheck = splitTitle[i].toLowerCase();

    if (charCheck.length > 2) {
      resultArray.push(charCheck.charAt(0).toUpperCase() + charCheck.substring(1));
    } else {
      resultArray.push(charCheck);
    }
  }

  return resultArray.join(' ');
};

console.log(capitalizeTitle("capiTalIze tHe titLe"));