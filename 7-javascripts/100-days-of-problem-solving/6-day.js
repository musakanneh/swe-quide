/**
 * https://leetcode.com/problems/rank-transform-of-an-array/
 * @param {number[]} arr
 * @return {number[]}
 */
const arrayRankTransform = (arr) => {
    arr = [40, 10, 20, 30];
    let map = new Map();
    let sorted = [...new Set([...arr].sort((a, b) => a - b))];

    for (let i = 0; i < sorted.length; i++) {
        map.set(sorted[i], i + 1);
    }
    for (let i = 0; i < arr.length; i++) {
        arr[i] = map.get(arr[i]);
    }
    return arr;
};

console.log(arrayRankTransform());