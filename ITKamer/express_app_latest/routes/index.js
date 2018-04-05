const express = require('express');
const router = express.Router();


// root route or endpoint
router.get('/',(req, res) => {
    const name = req.cookies.username;
    if ( name ) {
        // render the index page
        res.render('index',{ name });
    } else {
        // redirect to the hello route
        res.redirect('/hello');
    }
});

// goodbye route or endpoint
router.post('/goodbye', (req, res) => {
    // clearing the cookie username
    res.clearCookie('username');
    // redirecting to the hello page
    res.redirect('/hello');
})
router.post('/begin', (req, res) => {
    // clearing the cookie username
    res.clearCookie('username');
    // redirecting to the hello page
    res.redirect('/hello');
})
// hello route or endpoint
router.get('/hello', (req, res) => {
    const name = req.cookies.username;
    if ( name ) {
        // redirect to the index page
        res.redirect('/');
    } else {
        // render the hello page
        res.render('hello');
    }
}); 
router.post('/hello', (req, res) => {
    // set a cookie
    res.cookie('username', req.body.username);
    // redirecting to the root route
    res.redirect('/');
});
// exporting the router object
module.exports = router;