function findMaxAverage(nums: number[], k: number): number {
    let sum = 0
    for (let i = 0; i < k; i++){
        let el = nums[i];
        sum += el;
    }
    let avg = sum / k;
    for (let i = k; i < nums.length; i++){
        let el = nums[i];
        sum -= nums[i - k]
        sum += el
        avg = Math.max(avg, sum / k);
    }
    return avg;
};