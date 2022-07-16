const wordPattern = (pattern, s) => {
    const splitString = s.split(' '); 

    if (splitString.length !== pattern.length) return false;
    const map = {};
    
    for (let i = 0; i < pattern.length; i++) {
      let letterFromPattern = pattern[i];
      let wordFromSplitString = splitString[i];

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