/**
 * https://leetcode.com/problems/3sum/submissions/
 * @param {number[]} nums
 * @return {number[][]}
 */
 function threeSum(nums, target = 0) {     
    let ret = [];
    if (nums.length < 3) {
        return ret;
    }
    nums.sort((a,b) => a - b);   

    for (let i = 0; i < nums.length - 2 && nums[i] <= target; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }
        for (var j = i + 1, k = nums.length - 1; j < k;) {            
            let sum = nums[i] + nums[j] + nums[k];
            if (sum < target) {
                j++; continue;
            } else if (sum > target) {
                k--; continue;
            } 
            ret.push([nums[i], nums[j], nums[k]]);        
            while (nums[j] === nums[j+1]) j++;
            while (nums[k] === nums[k-1]) k--;
            j++;
            k--; 
        }
    }
    return ret;
}