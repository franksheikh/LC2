function runningSum(numbers:number[]): number[] {
	const ps = [numbers[0]]
	for (let i = 1; i < numbers.length; i++){
		ps.push(ps[ps.length-1] + numbers[i]);
	}
	return ps;
}