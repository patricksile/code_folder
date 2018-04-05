// Problem:String Revisal (6kyu)
/*
Instructions
*/
// My Solution:
function dup(s) {

  let res = [];
  
  s.forEach( w => res.push(w.replace(/(.{1})\1+/g,'$1')));
  
  return res;
}

// My other solution:

let dup = s => s.map(w => w.replace(/(.)\1+/g,'$1'))

// Other Solutions:

// Solution: By warriors nazarisaak

function dup(s) {
  return s.map(x => x.replace(/[^\w\s]|(.)(?=\1)/gi, ""));
}

// Solution: By warriors ZED.CWT

dup=Q=>Q.map(Q=>Q.replace(/(.)\1+/g,'$1'))

// Solution: By warriors አወል እሸቱ

function dup(s) {
return s.map(e=>e.replace(/(\w)\1+/g,(s, m)=>m[0]))
};

// Solution: By warriors IGZmanuelMartinVivaldi

function dup(s) {
 return  s.map (w => w.replace(/(.)\1+/g,'$1'))
};