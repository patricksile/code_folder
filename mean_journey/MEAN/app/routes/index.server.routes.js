// First routing file
// Load the 'index' controller
const index = require('../controllers/index.server.controller');

// Define the route module method
module.exports = function(app) {

	// Mount the 'index' controller's 'render' method 
	app.get('/', index.render);
};
