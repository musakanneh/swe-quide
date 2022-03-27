/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const targetIndices = (nums, target) => {
    nums = [1, 2, 5, 2, 3]; target = 3;
    nums.sort((a, b) => a - b);
    let ans = [];

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === target) {
            ans.push(i);
        }
    }
    return ans;
};

console.log(targetIndices());
