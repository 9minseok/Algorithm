function solution(nums) {
    const getCnt = nums.length / 2;
    const setSize = new Set(nums).size;
    
    return setSize > getCnt ? getCnt : setSize;
}