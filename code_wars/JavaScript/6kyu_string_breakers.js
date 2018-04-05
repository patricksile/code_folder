// Problem:String Breakers (6kyu)
/*
Instructions
*/
// My Solution:
function stringBreakers(n, string){
  
  let res = ''; let pre_res = '';
 
  for(let i = 0; i < string.length; i++){
    
    if(string[i] === ' '){continue;}
 
    if(pre_res.length % n === 0 && pre_res.length > 0){
  
      res += pre_res + '\n';
      pre_res = '';  
    }  
    pre_res += string[i];
  }
  return res + pre_res
}

// Other Solutions:

// Solution: By warriors Voile

function stringBreakers(n, string){
  return string.replace(/[^a-zA-Z\d]/g,'').match(new RegExp(`.{${n}}|.+$`,'g')).join('\n')
}

// Solution: By warriors docgunthrop

const stringBreakers = (n,s) => s.replace(/ +/g,'').match(new RegExp(`.{1,${n}}`,'g')).join('\n');

// Solution: By warriors luisgc

function stringBreakers(n, string){
  return string.replace(/\s/g,"").match(new RegExp("\\w{1," + n + "}","g")).join("\n");
}


// Solution: By warriors ZED.CWT

stringBreakers=(N,Q)=>Q.replace(/\s/g,'').replace(RegExp(`.{${N}}(?!$)`,'g'),'$&\n')

// Solution: By warriors Almosawi

function stringBreakers(n, str){
    return str.replace(/\s/g,"").replace(new RegExp(`(.){1,${n}}`,"g"),m=>m+"\n").slice(0,-1)
}

// Solution: By warriors Unnamed

function stringBreakers(n, string) {
  string = string.replace(/ /g, '');
  return string && string.match(new RegExp(`.{1,${n}}`, 'g')).join('\n');
}

// Solution: By warriors myjinxin2015

stringBreakers=(n, s)=>(s.replace(/ /g,"").match(new RegExp(".{1,"+n+"}","g"))||[]).join`\n`

// Solution: By warriors Souzooka

function stringBreakers(n, string){
  let result = [];
  string = string.replace(/\s/g, "");
  
  for (let i = 0; i < string.length; i += n) {
    result.push(string.substr(i, n));
  }

  return result.join("\n");
}


