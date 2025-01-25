// O(n) time
// O(1) space
function isSubsequence(s: string, t: string): boolean {
    let si = 0;
    for (let i = 0; i < t.length; i++){
        if (s[si] === t[i]) si++;
    }
    return si === s.length;
};