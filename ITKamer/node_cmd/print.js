// Print Error Messages
function printError(error) {
    console.error(error.message);
}

// function to print message to console
function printMessage(username, badgeCount, point) {
    const message = `${username} has ${badgeCount} total badges(s) and ${point} points in JavaScript`;
    console.log(message);
}
///"The fee is" + (isMember ? '$2.00' : '$10.00');
// Exporting functions of this file. (printError and printMessage)
module.exports.error = printError;
module.exports.message = printMessage;