/* All the console logout functions for the Weather app */
// Message printing function
function printMessage (city, temperature) {
    console.log (`The current temperature in ${city} is ${temperature}F.`);
}
function printError (error) {
    console.error(`This is the error message: ${error.message}.`);
}
// Exporting functions or methods
module.exports.message = printMessage;
module.exports.error = printError;