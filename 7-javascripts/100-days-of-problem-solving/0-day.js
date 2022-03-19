/**
 * https://leetcode.com/problems/concatenation-of-array/
 * @param {number[]}
 * @return {number[]}
 */
 var getConcatenation = function(nums) {
    nums = [1, 2, 1]; let ans_array = [];

    for (let i = 0; i < nums.length; i++) {
        ans_array += nums[i];
    }

    let result = [nums + ans_array];
    console.log(result)
};
getConcatenation();