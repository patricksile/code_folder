// Problem:
/*

*/
// My Solution:
var num = 567;
var reconstruct = [];
while(num > 0) {
    reconstruct.unshift(Math.floor(num % 10));
    // num = Math.floor(num * 1e-1)
    num = Math.floor(num * 1e-1)
}
console.log(reconstruct.join(''), num);
// Other Solutions:
// Solution 1: By
