const displayObject = () => {
    const person = {
        name: "Musa",
        age: 30,
        hobbies: ['waterpolo', 'reading']
    }
    const { name, age } = person;
    console.log(name, age);
}
displayObject();