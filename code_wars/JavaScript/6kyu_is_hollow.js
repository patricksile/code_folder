// Problem: Is Hollow (6kyu)
/*

*/
// My Solution:
function isHollow(x){

    // function to count of elements with value 0
    var count = function(arr){return arr.filter(i => i == 0).length};

    var lx = x.length; var c = count(x);

    return c >= 3 && (lx - c) % 2 == 0 && count(x.slice(0, (lx -c) / 2)) == 0

    && count(x.slice((lx + c) / 2, lx)) == 0
}
console.log(isHollow([2,2,0,0,0,1,0]))
// Other Solutions:
// Solution 1: By arhigod

function isHollow(x){
  return /^(1*)0{3,}\1$/.test(x.map(x=>x?1:0).join(''))
}

// Solution 1: By Troy Wu

function isHollow(x) {

  if (x.length%2 != 0) {
    var mid = Math.floor(x.length/2)

    if (x[mid - 1] === 0 && x[mid + 1] === 0) {
      for (var d = 2; d <= (x.length - 1)/2; d++) {
        if ((x[mid - d] || x[mid + d]) && !(x[mid - d] && x[mid + d])) {
          return false
        }
      }
      return true
    }
    return false
  }

  else {
    var midR = x.length/2
    var midL = midR - 1

    if (x[midL - 1] === 0 && x[midR + 1] === 0) {
      for (var d = 2; d <= (x.length - 1)/2; d++) {
        if ((x[midL - d] || x[midR + d]) && !(x[midL - d] && x[midR + d])) {
          return false
        }
      }
      return true
    }
    return false
  }
}


// Solution 1: By yuchchen1314

function isHollow(x){
 var counter=0
 console.log(x)
 x.forEach(function(a){
   if(a===0) counter++
 })

 if(counter>2){
    var idx=x.indexOf(0)
    var lidx=x.lastIndexOf(0)+1
      if(x.slice(idx,lidx).length !==counter) return false
  if(x.slice(0,idx).length===x.slice(lidx).length) return true
  }

  return false
}
// Solution 1: By slw

function isHollow(x){
  let filtArr = x.filter(item => {
    return item != 0;
  });
  let firstZeroIndex = x.indexOf(0);
  let zeroCount = x.length - filtArr.length;
    return zeroCount >= 3 && firstZeroIndex === (x.length - zeroCount) / 2;
}
// Solution 1: By Save14

function isHollow (arr) {

  if (
    arr.length >= 3 &&
    arr.filter(el => el === 0).length === arr.length
  ) return true;

  if (arr[0] === 0 || arr[arr.length-1] === 0) return false;

  let acc = 0;
  let first = 0;
  let last = 0;

  arr.forEach(el => {
    if (el === 0) acc++;
    else if (acc < 3) {
      first++;
      acc = 0;
    } else last++;
  });

  if (first === last && acc >= 3) return true;
  return false;
}
// Solution 1: By iorme1

function isHollow(x){
 var prevCount = 0;
 var afterCount = 0;
 var count = 0;
 var zeroCount = 0;

 for (var i = 0; i < x.length; i++) {
    if(afterCount > 0 && x[i] !== 0) {
      afterCount++;
      continue;
    }
    if (x[i] !== 0 && x[i-1] !==0) {
      count++;
    } else if (x[i] === 0) {
      prevCount = count;
      zeroCount++;
    }
    else if (x[i-1] === 0 && x[i] !== 0) {
      afterCount++;
    }
 }

  if(afterCount == prevCount && zeroCount >= 3) {
    return true;
  } else {
    return false;
  }
}
// Solution 1: By አወል እሸቱ

function isHollow(x){
if(x.length<3) return false
let a=x.slice(0,x.indexOf(0)),
    b=x.slice(x.lastIndexOf(0)+1),
    c=x.slice(x.indexOf(0),x.lastIndexOf(0)+1);

return c.every(e=>e===0) && c.length>2&&
       a.every(e=>e!=0) &&
       b.every(e=>e!=0) && a.length===b.length
}
// Solution 1: By dasp24

const isHollow = (arr) => {
    if (arr.length < 3) return false
    const midIndex = Math.floor(arr.length / 2);
    const sol = true;
    const filtered =arr.filter(x=>x===0)
    if (filtered.length === arr.length) return sol;
    if (arr[midIndex] === 0 && arr[midIndex + 1] === 0 && arr[midIndex - 1] === 0 && arr[0] !== 0 && arr[arr.length - 1] !== 0) return true;
    else return false;
};
// Solution 1: By Almosawi

function isHollow(x){
    var first = x.slice(0, x.indexOf(0));
    var last = x.slice(x.lastIndexOf(0) + 1);
    var zeros = x.slice(x.indexOf(0), x.lastIndexOf(0) + 1);
    if(first.length !== last.length) return false;
    return zeros.join("") == "0".repeat(zeros.length) && zeros.length >= 3
}
// Solution 1: By pH77

function isHollow(array) {
  var binary = array.map(value => value === 0 ? 0 : 1).join('');
  return /^(1*)0{3,}\1$/g.test(binary);
}
// Solution 1: By ZozoFouchtra

function isHollow(x, x$=x.map(x=>+!!x).join`` ){
  return /^(1+)?000+(\1)$/.test(x$)
}
// Solution 1: By madameBovary

function isHollow(x){
  var low = x.indexOf(0);
  var high = x.lastIndexOf(0);
  return x.slice(low, high + 1).every(a => a === 0) && x.length - 1 - high === low && high - low >= 2
}



// Solution 1: By Souzooka

function isHollow(x){
  let preceding = 0;
  let following = 0;
  let zeroes = 0;

  for (let i = 0; i < x.length; ++i) {
    // checks if zeroes are not continous and exits early if so
    if (x[i] === 0 && preceding !== 0) {
      return false;
    }

    // counts zeros
    if (x[i] === 0) {
      ++zeroes;
    }

    // counts following or preceding
    if (x[i] !== 0) {
      if (zeroes === 0) { ++following; }
      else if (zeroes !== 0) { ++preceding; }
    }
  }

  return following === preceding && zeroes >= 3;
}
console.log(isHollow([4,5,0,0,0,6,7]))


// Solution 1: By luisgc

function isHollow(x){
  var left   = x.slice(0,x.indexOf(0)).filter(v => v !== 0).length;
  var middle = x.slice(x.indexOf(0),x.lastIndexOf(0) + 1);
  var right  = x.slice(x.lastIndexOf(0) + 1).filter(v => v !== 0).length;

  return middle.every(v => v === 0) && middle.length > 2 && left === right;
}
// Solution 1: By choupi17

function isHollow(x){
    var count = function(arr){return arr.filter(i => i == 0).length};
    var lx = x.length; var c = count(x);
    return c >= 3 && (lx - c) % 2 == 0 && count(x.slice(0, (lx -c) / 2)) == 0 && count(x.slice((lx + c) / 2, lx)) == 0 ? true : false;
}
// Solution 1: By kazk

function isHollow(xs) {
  const m = xs.map(b => +(b != 0)).join('').match(/0+|1+/g) || [];
  return (m.length == 3 && m[0].length == m[2].length && m[1][0] == '0' && m[1].length >= 3)
      || (m.length == 1 && m[0].length >= 3 && m[0][0] == '0');
}
// Solution 1: By docgunthrop

function isHollow(ar){
  const a = ar.indexOf(0),
      b = ar.lastIndexOf(0),
      zar = ar.slice(a,b+1),
      arA = ar.slice(0,a),
      arB = ar.slice(b+1);
  return zar.length > 2 && zar.every(e => e === 0) && arA.length === arB.length && [arA,arB].every(e => !e.includes(0));
}
// Solution 1: By K1ngMX

function isHollow(array){
  // zero / nonzero constraint
  for (var x = 0 ; x < array.length ; x++){
  var otherside = array.length - x - 1

    if (array[x] != 0){
      if (array[otherside] == 0)
        return false;
    } else {
      if (array[otherside] != 0)
        return false;
    }
  }

  // at least 3 zero in the middle constraint
  var middle = Math.floor(array.length / 2);
  if (array[middle] != 0 || array[middle+1] != 0 ||array [middle-1] != 0)
    return false;

  return true;

}
// Solution 1: By Unnamed

function isHollow(xs) {
  const i = xs.indexOf(0), j = xs.lastIndexOf(0);
  return j - i >= 2 && i == xs.length - j - 1 && xs.slice(i, j + 1).every(x => x == 0);
}
// Solution 1: By St3f4n

function isHollow(x){
  let a = x.indexOf(0), b = x.lastIndexOf(0);
  return a === x.length-b-1 && b-a>=2 && x.slice(a,b+1).every(v=>v===0);
}
// Solution 1: By smile67

function isHollow(a){
  var precCnt=0,zeroIndex=0, zeroCnt=0, followIndex=0, followCnt=0;
  for(var i=0; i<a.length; i++) if(a[i]!=0) precCnt++; else {zeroIndex=i; break}
  for(var i=zeroIndex; i<a.length; i++) if(a[i]==0) zeroCnt++; else {followIndex=i; break}
  for(var i=followIndex; i<a.length; i++) if(a[i]!=0) followCnt++; else break;
  return precCnt==followCnt&&zeroCnt>2
}
// Solution 1: By Voile

function isHollow(x){
  return /^(-?[1-9]\d*,)*0(,0){2,}(,-?[1-9]\d*)*$/.test(x) && x.indexOf(0) === x.length-1-x.lastIndexOf(0)
}
