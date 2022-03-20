"use strict";

/**
 * https://leetcode.com/problems/concatenation-of-array/
 * @param {number[]}
 * @return {number[]}
 */
var getConcatenation = function getConcatenation(nums) {
  nums = [1, 2, 1];
  var ans_array = [];

  for (var i = 0; i < nums.length; i++) {
    ans_array += nums[i];
    console.log(ans_array);
  }

  var result = nums.concat(ans_array);
  console.log(result);
};

getConcatenation();