// n[i] > n[len - 1]  - n[i]
function waysToSplitArray(nums: number[]): number {
    let splits = 0;
    const l = nums.length;
    const ps = [nums[0]]
    for (let i = 1; i < nums.length; i++){
        ps.push(nums[i] + ps[ps.length - 1])
    }
    
    for (let i = 0; i < nums.length - 1; i++){
        let li = ps[i];
        let ri = ps[l - 1];
        let diff = ri - li
        if (li >= diff) splits++;
    }
    return splits;
};