// Problem: We neeed a simple way to look at a user's badge count and JS points
// Solution: Use Node.js to connect to Treehouse's API to get profile information to print out.
// function to print message to console
function printMessage(username, badgeCount, point) {
    const message = `${username} has ${badgeCount} total badges(s) and ${points} points in JavaScript`;
    console.log(message);
}
printMessage("chalkers", 100, 2000000);

// Connect to the API URL (https://teamtreehouse.com/username.json)
// Read the data
// Parse the data
// Print the data