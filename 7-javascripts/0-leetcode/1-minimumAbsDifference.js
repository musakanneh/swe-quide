#!/usr/bin/node

/**
 * Input: arr = [4,2,1,3]
 * Output: [[1,2],[2,3],[3,4]]
 * @param {*} arr
 */

let minimumAbsDifference = (arr = [1, 3, 6, 10, 15]) => {
  /**
   * Return a list of pairs in ascending
   * order(with respect to pairs), each pair [a, b] follows
   */
  arr.sort((a, b) => a - b);
  let minimumDifference = Infinity;
  let result = [];

  for (let i = 0; i < arr.length - 1; i++) {
    let actualDifference = arr[i + 1] - arr[i];
    minimumDifference = Math.min(actualDifference, minimumDifference);
  }

  for (let i = 0; i < arr.length - 1; i++) {
    let actualDifference = arr[i + 1] - arr[i];
    if (minimumDifference === actualDifference) {
      result.push([arr[i], arr[i + 1]]);
    }
  }

  console.log(result);
};

let findMinimumDiff = (arr) => {
  /**
   * Return the minimum number in a given array
   */
  let minNum = 0;
  console.log(minNum);
};

/**
 * Functions control
 */
// minimumAbsDifference();
// findMinimumDiff();
minimumAbsDifference();
