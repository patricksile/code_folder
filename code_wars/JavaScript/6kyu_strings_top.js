// Problem:
/*

*/
// My Solution:
function tops(msg) {
  i = 1, d = 5, s = '';
  while(i < msg.length){
    s += msg[i]
    i += d
    d += 4
  }
   return s.split('').reverse().join('')
}
// Other Solutions:
// Solution 1: By
function tops(msg) {

  let top = '';
  let j = 1;

  for (let i = 0;;i++) {

    if (j > msg.length) {
      return top.split('').reverse().join('');
    }

    top += msg[j];

    j += 5 + i * 4;

  }

}
