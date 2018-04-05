// Problem: Stop gninnipS My sdroW (6kyu)
/*
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.


Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"
*/
// My Solution:
function spinWords(strg) {
  var spl = strg.split(' ')
  var newStrg = ""
  for (i = 0; i < spl.length; i++) {
  	if (spl[i].length >= 5) {
    	newStrg += ' ' + spl[i].split('').reverse().join('');
  	}
    else{
    	newStrg += ' ' + spl[i]
    }
	}
  return newStrg.slice(1)
 }

 // console.log("Hello World")
// Other Solutions:
// Solution 1: By katzoo, colbydauph, Fishythefish, Polina, aertmann, stephenmu

function spinWords(words){
  return words.split(' ').map(function (word) {
    return (word.length > 4) ? word.split('').reverse().join('') : word;
  }).join(' ');
}

// Solution 2: By mortonfox, pro2501, abatvsurin, gdevpura, user5494429

function spinWords(string){
  return string.replace(/\w{5,}/g, function(w) { return w.split('').reverse().join('') })
}

// Solution 3: By curious_db97, appsincaps, LegacyCrono, oleksaly

function spinWords(str){
  return str.split(' ').map( w => w.length<5 ? w : w.split('').reverse().join('') ).join(' ');
}
