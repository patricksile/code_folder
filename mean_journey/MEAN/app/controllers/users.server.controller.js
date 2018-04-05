// Load the 'User' Mongoose model
const User = require('mongoose').model('User'); // returns the User model previously define

// Create a new 'create' controller method
exports.create = function(req, res, next) {

	// Create a new instance of the 'User' Mongoose model
	const user = new User(req.body);

	// Use the 'User' instance's 'save' method to save a new user document
	user.save((err) => {

		if (err) {

			// Call the next middleware with an error message
			return next(err);

		} else {

			// Use the 'response' object ot send a JSON response
			res.status(200).json(user);
		}
	});
};

// Create a new 'delete' controller method
exports.delete = function(req, res, next) {
	// Use the 'User' instance's 'remove' method to save a new user document
	req.user.remove((err) =>{

		if (err) {
			// Call the next middleware with an error message
			return next(err);
		} else {
			// Use the 'response' object to send a JSON response
			res.status(200).json(req.user);
		}
	})
}

// Create a new 'list' controller method
exports.list = function(req, res, next) {

	// Use the 'User' static 'find' method to retrieve the list of users
	User.find({},'username email', (err, users) =>{

		if (err) {

			// Call the next middleware with an error message
			return next(err);

		} else {

			// Use the 'response' object to send a JSON response
			res.status(200).json(users);
		}
	});
};

// Create a new 'read' controller method
exports.read = function(req, res) {

	// Use the 'response' object to send a JSON response
	res.json(req.user);
};

// Create a new 'userByID' controller method
exports.userByID = function(req, res, next, id) {
	// Use the 'User' static 'findone' method to retrieve a specific user
	User.findOne( {_id: id}, (err, user) => {

		if (err) {

			// Call the next middleware with an error message
			return next(err);
		} else {
			// Set the 'req.user' property
			req.user = user;

			// Call the next middleware
			next();
		}
	})
};

// Create a new 'update' controller method
exports.update = function(req, res, next) {

	// Use the 'User' static 'findByIdAndUpdate' method to update a specific user
	User.findByIdAndUpdate(req.user.id, req.body, {new: true}, (err, user) => {

			if (err) {
				// Call the next middleware with an error message
				return next(err);
			} else {
				// Use the 'response' object to send a JSON response 
				res.status(200).json(user);
			}
	});
};

