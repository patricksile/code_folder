// Problem:Commong data type (6kyu)
/*
Find the most common Data Type within a given array.

For Example, ['1', '2', 2] should return 'string'.

If there are any ties at all then just return 'We got a tie!'
*/
// My Solution:
// class CommonDatatypes {
  
  function check(arr){

    let type_arr = arr.map(x => typeof x)
    let max_type = ''; let count = 0; let current = 0; let track = [];
    
    new Set(type_arr).forEach( type =>{

         
      current = type_arr.filter(a => a == type).length;

      track.push(current);

      if(current > count){

      	count = current;
      	max_type = type;

      }
      
    })
    return track.filter(a => a === count).length > 1 ? 'We got a tie!' : max_type

  }
// }

console.log(check([true,true, true, true, 12, 'yo']))
// Other Solutions:

// Solution: By warriors