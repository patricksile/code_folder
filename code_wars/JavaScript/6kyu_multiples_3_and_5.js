// Problem:Multiples of 3 and 5 (6kyu)
/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.
Courtesy of ProjectEuler.net
*/
// My Solution:
function solution(number){

  if(number < 0){return 0;}
  
  let valid = 0;
  
  Array.from(new Array(number), (x,i) => i).forEach( i => {
  
    if(i % 3 === 0 || i % 5 === 0){valid += i;}
  })
  return valid;
}
// Other Solutions:

// Solution: By warriors ylxx

solution= n=> n<=0?0:Array.from({length: n}, (_,i) => (i%3==0||i%5==0)?i:0).reduce((x,y)=>x+y)


// Solution: By warriors Johffner

function solution(number){
  var sum = 0;
  
  for(var i = 1;i< number; i++){
    if(i % 3 == 0 || i % 5 == 0){
      sum += i
    }
  }
  return sum;
}