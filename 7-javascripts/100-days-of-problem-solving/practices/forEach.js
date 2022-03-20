const print_sum = (nums) => {
    let sum = 0;
    arr = [10, 20, 30, 40, 50];
    // nums.forEach((arr, i) => {
    //     sum += arr[i];
    // })
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}

// console.log(print_sum())
let sum = 0;
const numbers = [65, 44, 12, 4];
numbers.forEach(myFunction);

function myFunction(item) {
    sum += item;
}
console.log(myFunction())