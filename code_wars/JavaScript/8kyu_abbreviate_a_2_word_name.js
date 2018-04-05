// Problem:
/*
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot seperating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F
*/
// My Solution:

function abbrevName(name){

    var splitName = name.split(' ')
    return splitName[0][0].toUpperCase() + '.' + splitName[1][0].toUpperCase()

}
// Other Solutions:

// Solution 1: By sgmaster

function abbrevName(name){
  return name.split(' ').map(x => x.substr(0, 1).toUpperCase()).join('.');
}

// Solution 2: asweeney41, Exzorcist, pavellevap, marioepugh

function abbrevName(name){

  var nameArray = name.split(" ");
  return (nameArray[0][0] + "." + nameArray[1][0]).toUpperCase();
}

// Solution 3: By cneltyn, Odai-kakhi

function abbrevName(name){
  return name.match(/\b(\w)/g).toString().toUpperCase().replace(',', '.');
}

// Solution 4: By narayanswa30663, grek-andrian

function abbrevName(name){

    return name.split(' ').map(i => i[0].toUpperCase()).join('.')

}

// Solution 5: By Beast

const abbrevName = name => name.match(/\b\w/g).join('.').toUpperCase()

// Solution 6: By mozart

abbrevName = n => `${(n = n.toUpperCase().split(' '))[0][0]}.${n[1][0]}`

// Solution 7: By pgrzesik

function abbrevName(name){
  splitted = name.split(" ");
  return `${splitted[0][0]}.${splitted[1][0]}`.toUpperCase()
}
