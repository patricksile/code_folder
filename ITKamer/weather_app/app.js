/* Application file */
// Require the Weather information of a city
// Require weather file
const weather = require('./weather');

// Using the `process` object and his mehtod `argv`
const city = process.argv.slice(2).join();
// Calling the cityWeather(city) method of the weather file and going through each of the locationId
// city.length < 2 ? weather.cityTemp(city[0]) : weather.cityTemp(city[0] + ',' + city[1]) 


