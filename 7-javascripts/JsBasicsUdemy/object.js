#!/usr/bin/node

let jsObject = () => {
  let person = {
    name: "Musa",
    age: 30,
  };

  if (person.name !== "Musa") {
    console.log("Not the name");
  } else {
    console.log("That's the name buddy");
  }

  console.log(person);
};

jsObject();
