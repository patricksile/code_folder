// Load the 'Users' controller
const users = require('../../app/controllers/users.server.controller');

// Define the routes module method
module.exports = function(app) {

	// Set up the 'users' base routes
	app.route('/users')
	   .post(users.create)
	   .get(users.list);

	// Set up the 'users' parmeterized routes
	app.route('/users/:userId')
	   .get(users.read)
	   .put(users.update);

	// Set up the 'UserId' parameter middleware
	app.param('userId', users.userByID);

};


