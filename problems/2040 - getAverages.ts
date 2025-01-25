// Prefix_Sum
function getAverages1(nums: number[], k: number): number[] {
    const r = k * 2 + 1
    const avgs = Array(nums.length).fill(-1)
    if (r > nums.length){
        return avgs;
    }
    if (k===0){
        return nums
    }
    const prefix_sum = Array(nums.length + 1).fill(0);
    for (let i = 0; i < nums.length; i++){
        prefix_sum[i+1] = prefix_sum[i] + nums[i]
    }
    
    for (let i = k; i < nums.length - k; i++){
        let sum = prefix_sum[i + k + 1] - prefix_sum[i - k]
        avgs[i] = Math.floor(sum / r);
    }
    
    return avgs;
};
// My solution
// O(n) time
// O(n) space
function getAverages2(nums: number[], k: number): number[] {
    const avgs = Array(nums.length).fill(-1);
    const radius = 2 * k + 1
    if (radius > nums.length) {
        return avgs
    }
    if (k === 0){
        return nums
    }
    let sum = 0;
    for (let i = 0; i < radius; i++){
        sum += nums[i];
    }
    avgs[k] = Math.floor(sum / radius)
    
    for (let i = k + 1; i < nums.length; i++){
        if (i+k < nums.length){
            sum -= nums[i - k - 1]
            sum += nums[i + k]
            avgs[i] = Math.floor(sum / radius);
        }
    }
    
    return avgs;
};