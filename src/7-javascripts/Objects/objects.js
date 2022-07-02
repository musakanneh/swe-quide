const FactoryFunction = (radius) => {
  return {
    radius,
    draw() {
      console.log("Cicle");
    },
  };
};

const Circle = (radius) => {
  this.radius = radius;
  this.draw = function() {
    console.log("Circle");
  };
};

const someObject = [
  {
    name: "Musa",
    age: "23",
  },
];

const printDetails = () => {
  return {
    name: "Musa",
    age: "23",
  };
};
console.log(printDetails());
