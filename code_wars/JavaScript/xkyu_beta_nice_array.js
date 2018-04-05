// Problem: Nice array(7kyu)
/*
A Nice array is defined to be an array where for every value n in the array, there is also an element n-1 or n+1 in the array.

example:

[2,10,9,3] is Nice array because

2=3-1
10=9+1
3=2+1
9=10-1
Write a function named isNice that returns true if its array argument is a Nice array, else false. You should also return false if input array has no elements.
*/
// My Solution:
function isNice(arr){
    var counter = 0
    for(var i = 0; i < arr.length; i++) {
        if (arr.includes(arr[i] - 1) || arr.includes(arr[i] + 1)){
            counter ++
        }
    }
    if(counter == arr.length && arr.length != 0) {
        return true
    }
    return false
}
console.log(isNice([]))

// Other Solutions:
// Solution 1: By smile67

function isNice(arr){
  for (var n of arr) if (!arr.includes(n-1)&&!arr.includes(n+1)) return false;
  return arr.length>0
}

// Solution 2: By kazk

function isNice(arr) {
  if (arr.length == 0) return false;
  const s = new Set(arr);
  return arr.every(x => s.has(x-1) || s.has(x+1));
}

// Solution 3: ByZED.CWT

isNice=(震,え,声)=>{for(震=震.filter((一,転)=>転==震.indexOf(一)).sort((攻,勢)=>攻-勢),え=0,声=!え;声&え<震.length;)1+震[え-1]==震[え]|1+震[え]==震[1+え]?++え:声=!9;return 声&&0<震.length}

// Solution 4: By Voile

function isNice(arr){
  var h=arr.reduce((h,n)=>(h[n]=true,h),{})
  return arr.length>0&&arr.every((e,i)=>h[e-1]||h[e+1])
}

// Solution 4: By totine

function isNice(arr){
  return arr.length>0 ? arr.every(x=> arr.some(y => y - 1 == x || y + 1 == x)) : false;
}

// Solution 5: By microorganisms

function isNice(arr) {
  const s = new Set(arr);
  for (let e of arr) {
    if (!s.has(e - 1) && !s.has(e + 1)) {
      return false;
    }
  }
  return !!arr.length;
}

// Solution: By luisgc

function isNice(arr){
  return arr.length > 0 && arr.every((v1,i) => arr.find((v2,j) => j !== i && Math.abs(v1 - v2) === 1) !== undefined);
}

JohanWiltink

const isNice = a => Boolean(a.length) && a.every( v => a.includes(v-1) || a.includes(v+1) ) ;

// Solution: By አወል እሸቱ

function isNice(arr){

  return arr.length>0 && arr.every(e=>arr.includes(e+1)||arr.includes(e-1))
}
