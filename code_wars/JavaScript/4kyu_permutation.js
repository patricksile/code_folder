
// Problem:Permutation 4kyu
/*
In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); // ['a']
permutations('ab'); // ['ab', 'ba']
permutations('aabb'); // ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
The order of the permutations doesn't matter.
*/
// My Solution:

function permutations(string) {

  if(string.length <= 1){return [string];}

  let perms = permutations(string.slice(1, string.length));
  let char = string[0];
  let result = [];

  perms.forEach(perm => {

    for(let i = 0; i <= perm.length; i++){

      result.push(perm.slice(0, i) + char + perm.slice(i, perm.length));
    }
  })

  return Array.from(new Set(result));  
}
console.log(permutations('aabb'))

// Other Solutions:

// Solution: By warriors Azuaron, MinionKevin, testtest123, jwong483, Vorgue, sharpskill (plus 19 more warriors)

function permutations(string) {

  var arr = string.split(''), tmp = arr.slice(), heads = [], out = [];

  if(string.length == 1) return [string];

  arr.forEach(function(v, i, arr) {

    if(heads.indexOf(v) == -1) {

      heads.push(v);
      tmp.splice(tmp.indexOf(v), 1);

      permutations(tmp.join('')).forEach(function(w) {out.push(v + w);});
      
      tmp.push(v);
    }
  });
  return out;
}

// Solution: Bythink2011, melanoman, willin, dubdjon, July

function permutations(string) {

  return (string.length == 1) ? [string] : string.split('').map(

     (e, i) => permutations(string.slice(0,i) + string.slice(i+1)).map((e2) => e+e2)

  ).reduce((r,e) => r.concat(e)).sort().filter((e,i,a) => (i==0) || a[i-1] != e);
}

// Solution: By evk

function permutations(str) {

 return (str.length <= 1) ? [str] :

         Array.from(new Set(

           str.split('')

              .map((char, i) => permutations(str.substr(0, i) + str.substr(i + 1)).map(p => char + p))

              .reduce((r, x) => r.concat(x), [])
         ));
}