class DisplayCharTypeInSentense {
  constructor(inputText) {
    this.inputText = inputText;
  }

  toLowerCase = (inputString) => {
    let letterCount = 0;
    while (letterCount < inputString.length) {
      return inputString.toLowerCase();
    }
    letterCount++;
  };

  uniqueInOrder = (iterable) => {
    let resArray = [];
    for (let i = 0; i < iterable.length; i++) {
      if (iterable[i] !== iterable[i + 1]) {
        resArray.push(iterable[i]);
      }
    }
    return resArray;
  };

  capitalizeTitle = (title) => {
    let resultArray = [];
    let splitTitle = title.split(" ");
    for (let i = 0; i < splitTitle.length; i++) {
      let charCheck = splitTitle[i].toLowerCase();
      if (charCheck.length > 2) {
        resultArray.push(
          charCheck.charAt(0).toUpperCase() + charCheck.substring(1)
        );
      } else {
        resultArray.push(charCheck);
      }
    }
    return resultArray.join(" ");
  };
}

console.log(toLowerCase("MusaKanneh"));
console.log(uniqueInOrder("AAAABBBCCDAABBB"));
console.log(capitalizeTitle("capiTalIze tHe titLe"));
