/* Weather data file */
// Require http module
const http = require('http');
// Require some files
const print = require('./print');
// Require some json
const api = require('./api.json');

// Basic get response function
function cityWeather(cityParameter) {

    // api access url
    const apiUrl = `http://api.openweathermap.org/data/2.5/forecast?` + eval("cityParameter.includes(',') ? 'q' : 'id'") + `=${cityParameter}` + `&APPID=${api.key}`;
    try {
        
        const request = http.get(apiUrl, response => {
            if (response.statusCode === 200) {
                    
                // Body of the weather data
                let body = "";
                // Read the Data
                response.on('data', data => {
                    body += data.toString();
                });
                response.on('end', () => {
                    try {
                        // Parse the weather data
                        const weatherData = JSON.parse(body);
                        // Print the weather Data
                        print.message(weatherData.city.name, weatherData.list[0].main.temp);
                    } catch (error) {
                        print.error(error);
                    }
                });
            } else {
                const message = `There was an error getting the weather data for ${cityParameter} error: (${http.STATUS_CODES  [response.statusCode]})`;
                const statusCodeError = new Error(message);
                print.error(statusCodeError);

            }
    });
    request.on('error', error => console.error(`Problem with request:${error.message}`));
    } catch (error) {
        print.error(error);
    }
}

// Export the cityWeather method
module.exports.cityTemp = cityWeather;