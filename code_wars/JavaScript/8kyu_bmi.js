// Problem: BMI (8kyu)
/*
Write function bmi that calculates body mass index (bmi = weight / height ^ 2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
*/
// My Solution
function bmi(weight, height) {
	console.log(weight, height);
  var BMI = weight / Math.pow(height, 2);
  if(BMI <= 18.5){
  	return "Underweight"
  }
  else if(BMI <= 25.0){
  	return "Normal"
  }
  else if(BMI <= 30.0){
  	return "Overweight"
  }
  else{
    return "Obese";
  }
}
// Other Solutions:
// Solution 1: By AbigailB, Riebow, anujp41, MtlJ1991, Jacob-Berk, kickh

function bmi(weight, height) {
  var result = weight/Math.pow(height,2)

  if (result <= 18.5) {
    return "Underweight";
  } else if (result <= 25) {
    return "Normal";
  } else if (result <= 30) {
    return "Overweight";
  } else {
    return "Obese";
  }

}

// Solution 2: By dcieslak

const bmi = (w, h, bmi = w/h/h) =>  bmi <= 18.5 ? "Underweight" :
                                    bmi <= 25 ? "Normal" :
                                    bmi <= 30 ? "Overweight" : "Obese";

// Solution 3: By Sagua

function bmi(weight, height) {
  var formula = (weight / Math.pow(height, 2));
  switch (true) {
    case formula <=18.5:
    return 'Underweight';
    case formula <=25.0:
    return 'Normal';
    case formula <=30:
    return 'Overweight';
    default:
    return 'Obese';

  }
}

// Solution 4: By njohnson7

function bmi(weight, height) {
  let b = weight / height**2;
  return b <= 18.5 ? 'Underweight' : b <= 25.0 ? 'Normal' : b <= 30.0 ? 'Overweight' : 'Obese';
}

// Solution 5: By user3359372

function bmi(weight, height) {
 let bmi = weight / (height * height);
 switch(true){
   case bmi <= 18.5:
     return "Underweight";
   case bmi <= 25.0:
     return "Normal";
   case bmi <= 30.0:
     return "Overweight";
   case bmi > 30:
     return "Obese";
  }
}

// Solution 6: By mozart

bmi = (w, h) => (w = w / h / h) > 30 ? 'Obese' : w > 25 ? 'Overweight' : w > 18.5 ? 'Normal' : 'Underweight';

// Solution 1: By Krajan

function bmi(weight, height) {

var bmi  = weight/(height*height);

 return bmi < 18.5 ? "Underweight" : bmi <=25 ? "Normal" : bmi <= 30 ? "Overweight" : "Obese";

}

// Solution 7: By ooflorent

function bmi(weight, height) {
  const n = weight / height / height
  return n <= 18.5 ? "Underweight" : n <= 25 ? "Normal" : n <= 30 ? "Overweight" : "Obese"
