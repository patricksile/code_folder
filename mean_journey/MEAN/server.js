// Set the 'NODE_ENV' variable
process.env.NODE_ENV = process.env.NODE_ENV || 'development';

// Load the 'mongoose' module from config folder (Should be loaded first)
const configureMongoose = require('./config/mongoose');
// Load the 'express' module from config folder
const configureExpress = require('./config/express');

// Create a new Mongoose connection instance
const db = configureMongoose();

// Create a new Express application instance.
const app = configureExpress();

// Use the Express application instance to listen to the port '3000'
app.listen(3000);

// Use the module.exports property to expose our Express application
module.exports = app;

console.log("We are in \"" + process.env.NODE_ENV + "\" environment")
console.log('Server running at http://localhost:3000/');