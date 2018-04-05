// Problem: Cube powerful (beta)
/*
A number n>0 is called cube-powerful if it is equal to the sum of the cubes of its digits. Write a function named isCubePowerful that return array of cube-powerful numbers below it. All inputs will be valid numbers.
*/
// My Solution:
function isCubePowerful(n){
	return [1,153,370,371,407].filter(x => n >= x);
}

function isCubePowerful(n){
  return n < 1 ? [] : n < 153 ? [1] : n < 370 ?
  [1,153] : n < 371 ? [1,153,370] : n < 407 ?
  [1,153,370,371]: n >= 407 ? [1,153,370,371,407] : NaN
}
// Other Solutions:
// Solution 1: By <Souzooka

const isCubePowerful = (() => {
  const cubePowerfulNumbers = [1, 153, 370, 371, 407];

  return n => cubePowerfulNumbers.filter(v => v < n);
})();
// Solution: By ZozoFouchtra

const isCubePowerful = n => [1, 153, 370, 371, 407].filter(x=>n>=x);
// Solution: By JohanWiltink

const memo = fn => ( cache => n => cache.has(n) ? cache.get(n) : cache.set(n,fn(n)).get(n) ) ( new Map() ) ;
String.prototype.reduce = Array.prototype.reduce;
const isCP = memo( n => String(n).reduce( (acc,v) => acc + Number(v)**3 , 0 )===n );
const isCubePowerful = n => Array.from( { length: n }, (_,i) => i+1 ).filter(isCP) ;
// Solution: By choupi17

function isCubePowerful(n){
  return [1,153,370,371,407].filter(x => n >= x);
}

// Solution: By docgunthrop

function isCubePowerful(n){
  const troll = [1,153,370,371,407],//🤡
      z = troll.findIndex(e => e > n);
  return z === -1 ? troll : troll.slice(0,z);
}
// Solution: By Unnamed

function isCubePowerful(n) {
  function isCubePowerful(n) {
    return n == Array.from(n.toString(), x => x ** 3).reduce((a, b) => a + b);
  }
  let res = [];
  for (let i = 1; i < n; i++)
    if (isCubePowerful(i))
      res.push(i);
  return res;
}
// Solution: By St3f4n

function isCubePowerful(n){
  return Array.from({length: n}, (v,i)=>i+1).filter(v=>cubePower(v));
}

function cubePower(n) {
  return (''+n).split('').reduce((a,b)=>a+b**3,0) === n;
}
// Solution: By myjinxin2015

function isCubePowerful(n){
  for(var r=[],i=1;i<n;i++) if(iscube(i)) r.push(i)
  return r
}
function iscube(n){
  return (n+"").split``.reduce((a,b)=>a+b**3,0)==n
}

// Solution: By Voile

const isCubePowerful=n=>[1,153,370,371,407].filter(m=>m<n)
// Solution: By smile67

function isCubePowerful(num){
  var r=[];
  for (var n=1;n<num;n++) if ([...n+''].reduce((s,a)=>+a*+a*+a+s,0)==n) r.push(n);
  return r
}
// Solution: By TehOrange

var cp = []


for (var i=1; i<10000; i++) cPow(i) ? cp.push(i) : undefined


function isCubePowerful(n){
  var res = []
  for (var j of cp) if(j<n){res.push(j)} else{break}
  return res
}


function cPow(n){
  return [...''+n]
         .map(e=>Math.pow(Number(e), 3))
         .reduce((x,y)=>x+y) == n
}
// Solution: By ZED.CWT

isCubePowerful=草=>[1,153,370,371,407].filter(生=>草>生)
// Solution: By አወል እሸቱ

function isCubePowerful(n){
  let a=[];
  for(let i=1;i<n;i++){
      if([...''+i].map(e=>(+e)**3).reduce((a,b)=>a+b)===i) a.push(i)
  }
  return a
}
