// Official
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
const numSubarrayProductLessThanK = function(nums, k) {
    if (k <= 1) {
        return 0;
    }

    let ans = 0, left = 0, curr = 1;
    
    for (let right = 0; right < nums.length; right++) {
        curr *= nums[right];
        while (curr >= k) {
            curr /= nums[left];
            left++;
        }
        
        ans += right - left + 1;
    }
    
    return ans;
};

// My Implementation
function numSubarrayProductLessThanK2(nums: number[], k: number): number {
    let runningProduct = 1;
    let count = 0;
    let window_items: number[] = [];
    let windowIdx = 0;

    for (let i = 0; i < nums.length; i++){
        let num = nums[i];
        runningProduct *= num;
        window_items.push(num)
        
        while (runningProduct >= k){
            runningProduct /= window_items[windowIdx];
            windowIdx++;
        }

        if (runningProduct < k){
            count += 1 + ((window_items.length - windowIdx) - 1);
        }
    }
    return count;
};