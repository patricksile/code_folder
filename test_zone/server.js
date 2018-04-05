// // Test of extends in classes

// class Vehicle{

// 	constructor(wheels) {

// 		this.wheels = wheels;
// 	}

// 	toString() {

// 		return '(' + this.wheels + ')';
// 	}
// }

// class Car extends Vehicle {

// 	constructor(color) {

// 		super(4);
// 		this.color = color;
// 	}

// 	toString() {

// 		return super.toString() + ' colored: ' + this.color;
// 	}
// }

// let car = new Car('blue');


// console.log(car.toString());
// console.log(car instanceof Car);
// console.log(car instanceof Vehicle);


// // Test of var, let and const


// function iterateVar() {

// 	for(var i = 0; i < 3; i++) {

// 		console.log(i)
// 	}
// 	console.log(i + "This is the after VAR")
// }


// function iterateLet() {

// 	for(let i = 0; i < 3; i++) {

// 		console.log(i)
// 	}
// 	// console.log(i + " This is LET") // Error had to happen here
// }

// const me = "Patrick"
// // me = "n" // This will have to throw an error cause we have 

// console.log(iterateVar())
// console.log(iterateLet()) // Error had to happen here


// // Starting a server on node.js
// const http = require('http');

// http.createServer((req, res) => {

// 	res.writeHead(200, {

// 		'Content-Type': 'text/plain'
// 	});

// 	res.end('Hello World');

// }).listen(80);
// console.log('Server running at http://localhost:3000/');


// Starting a server app with connect

const connect = require('connect');
const app = connect();

// Logger funciton
function logger(req, res, next) {

	console.log(req.method, req.url);
	next();
};


function helloWorld(req, res, next) {

	// Set the response content type header
	res.setHeader('Content-Type', 'text/plain');
	// Set the response text
	res.end('Hello people, there is no such a thing...');
};

// function goodbyeWorld
function goodbyeWorld(req, res, next) {
	// Set the response content type header
	res.setHeader('Content-Type', 'text/plain');
	// Set the response text
	res.end('Goodbye World then who gives a shit!');
};

// Register the middleware logger function with app and mounting a path
app.use(logger);
// Register the middleware helloWorld function with app and mounting a path
app.use('/hello',helloWorld);
// Register the middleware goodbyeWorld function with app and mounting a path
app.use('/goodbye', goodbyeWorld);
// Listening on port 80
app.listen(80);
console.log("Server running at http://localhost:80");
