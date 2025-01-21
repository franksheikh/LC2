function longestOnes(nums: number[], k: number): number {
    let l = 0, r = 0, c = 0;
    let max = 0

    for (let r = 0; r < nums.length; r++){
        let num = nums[r];
        if (num === 0) c++
        while (c > k){
            if (nums[l] === 0){
                c--;
            }
            l++
        }
        max = Math.max(max, r - l + 1)
    }

    return max
};