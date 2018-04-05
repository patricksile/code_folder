// Problem: We neeed a simple way to look at a user's badge count and JS points
// Solution: Use Node.js to connect to Treehouse's API to get profile information to print out.

// Require the profile module
const profile = require('./profile');

/* Using the `process` obj with his `argv` mtd to make the parameters be available from the command line as options and we have to slice the returned array from 2. */
const users = process.argv.slice(2);
users.forEach(profile.get);