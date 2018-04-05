// Problem:Vasya clerk (6kyu)
/*
Instructions
*/
// My Solution:
function tickets(client){

  let b25 = 0; let b50 = 0; let j = 0;
  
  for(let i = 0; i < client.length; i++){
  
    if(client[i] === 25){b25 += 25; ++j;}
    
    if(client[i] === 50 && b25 >= 25){b50 += 50; b25 -= 25; ++j;}
    
    if(client[i] === 100 && b50 >= 50 && b25 >= 25){b50 -= 50; b25 -= 25; ++j;}
    
    if(client[i] === 100 && b25 >= 75){b25 -= 75; ++j;}
  }
  return j === client.length ? 'YES':'NO'
}

console.log(tickets([25,25,50]))
// Other Solutions:

// Solution: By warriors	