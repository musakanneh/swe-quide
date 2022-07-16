var isIsomorphic = function(s, t) {
  let myMap = new Map();
  myMap.set(1, 'Musa');
  myMap.forEach(function(value, key){
      console.log(value + " " + key);
  })
};
console.log(isIsomorphic(s = "egg", t = "add"));
