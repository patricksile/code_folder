// Problem: N_centered (beta 6kyu)
/*
An array is called centered-N if some consecutive sequence of elements of the array sum to N and this sequence is preceded and followed by the same number of elements.

Example:

[3,2,10,4,1,6,9] is centered-15
because the sequence 10,4,1 sums to 15 and the sequence
is preceded by two elements [3,2] and followed by two elements [6,9]
write a method called isCenteredN that returns true if its array argument is not empty and centered-N but the inner array might be empty and that sum will be 0,otherwise it returns false.
*/
// My Solution:
function isCenteredN(arr,n){
    if(arr.length < 1) return false
    var counter = 0;
    while(counter <= parseInt(arr.length / 2)) {
        if(eval(arr.slice(counter, arr.length - counter).join('+')) == n)return true
        if(counter == arr.length / 2 && n == 0)return true
        counter ++;
    }
    return false
}
a = [1,2,3,5]
n = 1
console.log(isCenteredN(a,n))
// Other Solutions:
// Solution 1: By KenKamau

function isCenteredN(arr,n){
 for (var i = 0; i < arr.length; i++){
     if ((arr.slice(i,(arr.length - i))).reduce((a, b) => a + b, 0) == n)
         return true
 }
 return false

}

// Solution 2: By Unnamed

function isCenteredN(arr, n) {
  let m = (arr.length - 1) / 2, i = Math.ceil(m), j = Math.floor(m), s = i == j ? arr[i] : 0;
  while (i > 0 && s != n)
    s += arr[--i] + arr[++j];
  return s == n;
}

// Solution 3: By ZozoFouchtra

function isCenteredN(arr,n){
  let sum = arr.reduce((s,v)=>s+v,0), len = arr.length, x = 0;
  while( sum!=n && x<len>>1 ){
    sum -= (arr[x++] + arr[len-x]);
  }
  return sum==n
}

// Solution 4: By JohanWiltink

const sum = a => a.reduce( (v,w) => v+w , 0 ) ;
const isCenteredN = (a,n) => a.length!==0 && ( n===0 && a.length===2 || sum(a)===n || isCenteredN(a.slice(1,-1),n) ) ;
// Solution 5: By Voile

function isCenteredN(arr,n){
  if(!arr.length) return false;
  var i=0, j=arr.length-1, s=arr.reduce((s,n)=>s+n,0);
  if(s===n) return true;
  while(i<j) {
    s-=arr[i++]+arr[j--];
    if(s===n) return true;
  }
  return s===n;
}
// Solution 6: By luisgc

function isCenteredN(arr,n){
  for(var i = 0; i < arr.length; i++) {
    for(var j = i + 1; j < arr.length + 1; j++) {
      if(arr.slice(i,j).sum() === n && i === arr.length - j) { return true; }
    }
  }

  return false;
}

Array.prototype.sum = function() {
  return this.reduce((a,b) => a + b, 0);
}
// Solution 7: St3f4n

function isCenteredN(arr,n){
  let s = a => a.reduce((x,y)=>x+y,0);
  return arr.some((v,i)=>s(arr.slice(i,arr.length-i)) === n);
}
// Solution 8: By docgunthrop

function isCenteredN(ar,n){
  if (!ar.length){return false}
  const ln = ar.length - 1,
      hl = ar.length / 2 | 0,
      ix = ar.slice(0,hl).map((e,i) => e + ar[ln-i]);
  let z = ln % 2 ? 0 : ar[hl];
  while (ix.length && z !== n){z += ix.pop()}
  return z === n;
}

// Solution 9: By myjinxin2015

function isCenteredN(数组,数字){
   const 真=true,假=false
   for(var 长度=数组.length,左=(长度-长度%2)/2-1,右=(长度+长度%2)/2,和=长度%2?数组[(长度-1)/2]:0;长度>0&&左>=-1;和+=数组[左--]+数组[右++])
     if(和==数字) return 真;
   return 假
}
// Solution 10: By ZED.CWT

isCenteredN=(ア,ハ,八,ノ,ヽ)=>{for(ノ=ア.length,ヽ=1&ノ?ア[八=ノ>>=1]:ア[ノ/=2]+ア[八=ノ-1];0<=八&&ヽ!=ハ;)ヽ+=ア[++ノ]+ア[--八];return ヽ==ハ}

// Solution 11: By JohanWiltink

const plus = (v,w) => v+w ;
const sum = a => a.reduce(plus,0) ;
const isCenteredN = (a,n) => a.length!==0 && ( sum(a)===n || isCenteredN(a.slice(1,-1),n) ) ;
// Solution 12: By አወል እሸቱ

function isCenteredN(arr,n){
if(arr.length<1) return false
if(arr.reduce((a,b)=>a+b)===n) return true
for(let i=1;i<=~~(arr.length/2);i++){
    if(arr.slice(i,-i).reduce((a,b)=>a+b,0)===n) return true
  }
 return false
}
