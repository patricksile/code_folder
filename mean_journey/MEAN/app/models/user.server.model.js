// Load the Mongoose module and Schema object
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// Define a new 'UserSchema'
const UserSchema = new Schema({

	firstName: String,
	lastName: String,
	email: String,
	username: String,
	password: String
});


// Create the 'User' model out of the 'UserSchema'
mongoose.model('User', UserSchema);