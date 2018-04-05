// Problem:
/*
Given the string representations of two integers, return the string representation of the sum of those integers.

For example:

sumStrings('1','2') // => '3'
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

*/
// My Solution:
// function sumStrings(a,b) {
//   a == '' ? a = 0 : a = parseInt(a);
//   b == '' ? b = 0 : b = parseInt(b);
//   ab = a + b;
//   res = [];
//   while(ab > 0){
//   	res.unshift(ab % 10);
//     ab = Math.floor(ab * 1e-1);
//   }
//   return res.join('')
// }
function sumStrings(a,b){

    al = a.length; bl = b.length;
    al > bl ? b = '0'.repeat(al - bl) + b: al < bl ? a = '0'.repeat(bl - al) + a : null
    carry_over = '0'; temp = '0'; sum = ''; i = a.length - 1;
    while(i >= 0){
        temp = String(eval(a[i] + '+' + b[i] + '+' + carry_over))
        if (temp.length > 1){
            sum = temp[1] + sum;
            carry_over = temp[0];
        }
        else{
            sum = temp + sum;
            carry_over = '0'
        }
        --i
    }
    return (carry_over + sum).replace(/^0+/g, '')

}
console.log(sumStrings('99','000099'))

function add(a,b){
  a = a.split(''); b = b.split('');
  let sum = ''; let c  = 0;
  while(a.length || b.length || c){
    c += ~~a.pop() + ~~b.pop();
    sum = c % 10 + sum;
    c = c > 9;
  }
  return sum.replace(/^0+/, '');
}
 //,'579'
// console.log(sumStrings('112354334795495743957345874979534875','45654354354803598340958902849058384')) //,'579'
// Other Solutions:
// Solution 1: By student003, suva, seymoreskinner, alexch_, M.Syun, dpr980 (plus 33 more warriors)

// function sumStrings(a, b) {
//   var res = '', c = 0;
//   a = a.split('');
//   b = b.split('');
//   while (a.length || b.length || c) {
//     c += ~~a.pop() + ~~b.pop();
//     console.log(c,' and a ', ~~a.pop())
//     res = c % 10 + res;
//     c = c > 9;
//   }
//   return res.replace(/^0+/, '');
// }

// Solution : By MrSoto

// function sumStrings(aa, bb) {
//   var res = '', c = 0;
//   a = Array.from(aa);
//   b = Array.from(bb);
//   // console.log(a, ' and ', b)
//   while (a.length || b.length || c) {
//     c += (a.pop()||0) + (b.pop()||0);
//     // console.log(c)
//     res = c % 10 + res;
//     // console.log(res)
//     c = c > 9;
//   }
//   return res.replace(/^0+/, '');
// }
// console.log(sumStrings('768515', '180306'))
