/**
 * https://leetcode.com/problems/sum-of-all-odd-length-subarrays/submissions/
 * @param {number[]} arr
 * @return {number}
 */
 var sumOddLengthSubarrays = function(arr) {
    let sum = 0;
    
    for (let i = 0; i < arr.length; i++) {
        for (let j = i; j < arr.length; j++) {
            let sub_arr_len = j - i + 1;
            let is_sub_arr_odd = sub_arr_len % 2 !== 0;
            if (!is_sub_arr_odd) {
                continue;
            }
            for (let k = i; k <= j; k++) {
                sum += arr[k];
            }
        }
    }
    return sum;
};