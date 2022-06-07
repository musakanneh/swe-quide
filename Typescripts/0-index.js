const addPerson = (_data) => {
    const person = { data: ["Musa"] };
    person.data.push(_data);
    return person;
}
console.log(addPerson("Kanneh"));