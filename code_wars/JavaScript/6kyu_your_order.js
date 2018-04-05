// Problem:Your order please (6kyu)
/*
Your order, please

Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

your_order("is2 Thi1s T4est 3a")
[1] "Thi1s is2 3a T4est"
*/
// My Solution:

function order(words){
  
  // replace all letters by and empty space
  let digits_string = words.replace(/[a-z]/gi,'').split` `;

  // Splitted words

  let words_array = words.split` `;

  //new Object

  let words_dictionary = new Object();

  // loop in digits_string

  digits_string.forEach(

  	digit => words_dictionary[digit] = words_array[digits_string.indexOf(digit)]

  	)


  return (Object.values(words_dictionary)).join(' ')
}


// My second solution

function order(words){
  
  // replace all letters by and empty space
  let digits_string = words.replace(/[a-z]/gi,'').split` `;

  // split words
  let words_array = words.split` `;

  // new Array to collect each word in order 
  let result = [];

  // loop through digits_string
  digits_string.forEach( digit => result[+digit - 1] = words_array[digits_string.indexOf(digit)]);

  return (result).join(' ');
}

// My third solution 

function order(words){
  
  // replace all letters by and empty space
  let digits_string = words.match(/\d/g);

  // split words
  let words_array = words.split` `;

  // new Array to collect each word in order 
  let result = [];

  // loop through digits_string
  digits_string.forEach( digit => result[+digit - 1] = words_array[digits_string.indexOf(digit)]);

  return (result).join(' ');
}

// My forth solution

var order = words => words.split` `.sort((a,b) => a.match(/\d/) - b.match(/\d/)).join` `;

words = "is2 Thi1s T4est 3a"
console.log(order(words))
// Other Solutions:

// Solution: By warriors