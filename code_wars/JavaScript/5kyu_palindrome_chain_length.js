// Problem:
/*

*/
// My Solution:
var palindromeChainLength = function(n) {
  let i = 0;
  const rev = x => String(x).split('').reverse().join('');
  while(String(n) != rev(n)){
    n = n + parseInt(rev(n));
    ++i;
  }
  return i;
};
console.log(palindromeChainLength(87))
// Other Solutions:
// Solution 1: By
