// Problem:
/*

*/
// My Solution:
function solution(s){
  console.log(s);
  if(s.length % 2){s += '_'};
  ls = s.split('');
  rs = []
  ls.forEach(function(i){if (ls.indexOf(i) % 2 == 0){rs.push(i + ls[ls.indexOf(i) + 1])}})
  return rs

}
console.log(solution('abcdefg'))
// Other Solutions:
// Solution 1: By ZozoFouchtra, ooflorent, oneiro, JasonLough, RinGun, stoppre7

function solution(str) {
  return (str.length % 2 ? str + '_' : str).match(/../g);
}

// Solution 1: By prksingh, Assitan, kstag07, skhale, vedzmarka, michaeledwards1023

function solution(str){
  if (str.length%2) str += '_';
  return str.match(/.{1,2}/g)
}

// Solution 1: By tomtheisen, kroleg, Balkoth, mortonfox, Beast, Unnamed (plus 6 more warriors)

function solution(str){
   return (str + "_").match(/../g);
}


// Solution 1: By myjinxin2015

function solution(s){
   return (s+"_").match(/.{2}/g)||[]
}

gkucmierz

solution=s=>(s+'_').match(/../g)

Quazar

function solution(str){
   return (str.length % 2 ? str + '_': str).match(/\w\w/g);
}
