
// require the https module
const https = require('https');
// Require the http module
const http = require('http');
// require the print module
const print = require('./print');

// Connect to the API URL (https://teamtreehouse.com/username.json)
function get(username) {
    try {

        const request = https.get(`https://teamtreehouse.com/${username}.json`, response => {
            if (response.statusCode === 200) {


                let body = "";
                // Read the data

                response.on('data', data => {
                    body += data.toString();
                });
                response.on('end', () => {
                    try {
                        // Parse the data
                        const profile = JSON.parse(body);
                        // Print the data
                        print.message(username, profile.badges.length, profile.points.JavaScript);
                    } catch (error) {
                        print.error(error);
                    }
                });
            } else {
                const message = `There was an error getting the profile for ${username} error: (${http.STATUS_CODES[response.statusCode]})`;
                const statusCodeError = new Error(message);
                printError(statusCodeError);
            }

        });
        request.on('error', error => console.error(`Problem with request:${error.message}`));
    } catch (error) {
        print.error(error);
    }
}

// Exporting the get method
module.exports.get = get;