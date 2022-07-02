/**
 * https://leetcode.com/problems/concatenation-of-array/
 * @param {number[]}
 * @return {number[]}
 */
var getConcatenation = function (nums) {
    let ans = [];
    let num_len = nums.length;

    nums.forEach((nums, i) => {
        ans[i] = nums;
        ans[i + num_len] = nums;
    });

    return ans;
};
console.log(getConcatenation());