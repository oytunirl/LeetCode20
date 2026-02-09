function minOperations(nums: number[], k: number): number {
    // result
    let res: number = 0;

    for (let i = 0; i < nums.length; i++) {
        res += nums[i];
    }

    return res % k;
}