//API key from www.openweathermap.org 
// Sile = abccb7374f43fafffa55b8df8aa1dadb
// API JSON file url: http://api.openweathermap.org/data/2.5/forecast?id=<location_id>&APPID=<api_key>
// Test endpoint: http://api.openweathermap.org/data/2.5/forecast?id=2220957&APPID=8d52c6bcb6c2c8461f7292ce9e656245
/* Connect to the API URL */

// Location id of Yaounde Cameroon
// locationId = '2220957'
function endPointUrl(locationId){
    apiKey = '8d52c6bcb6c2c8461f7292ce9e656245';
    // api access url
    const apiUrl = `http://api.openweathermap.org/data/2.5/forecast?id=${locationId}&APPID=${apiKey}`
    return apiUrl
}
module.exports.url = endPointUrl;





