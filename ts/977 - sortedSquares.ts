function sortedSquares(nums: number[]): number[] {
	const a = Array(nums.length).fill(0);
	let i = nums.length - 1;
	let l = 0;
	let r = nums.length - 1;

	while (l <= r){
		let lAbs = nums[l] ** 2
		let rAbs = nums[r] ** 2
		if (rAbs > lAbs){
			a[i] = rAbs;
			r--
		}
		else {
			a[i] = lAbs;
			l++ 
		}
		i--;
	}
	return a;
};