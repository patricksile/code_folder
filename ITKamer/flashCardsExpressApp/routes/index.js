const express = require('express');
const router = express.Router();

// Creating the root route and serving the index template
router.get('/', (req, res) => {
    const name = req.cookies.username;
    // sending the index template to the root route if the cookie username value else redirect to the /hello route
    if (name) {
        res.render('index', { name });
    } else {
        res.redirect('/hello');
    }
});

router.get('/hello', (req, res) => {
    const name = req.cookies.username;
    // sending the index template to the root route if the cookie username value else redirect to the /hello route
    if (name) {
        res.redirect('/');
    } else {
        res.render('hello');
    }
});


// Creating the /hello route and serving the hello.pug template
router.get('/hello', (req, res) => {

    res.render('hello');
});

// For the Submit button
router.post('/hello', (req, res) => {

    res.cookie('username', req.body.username);
    // redirecting to the root route from /hello route
    res.redirect('/');
});

// GoodBye button to clear the cookie

router.post('/goodbye', (req, res) => {

    // Clearing the cookies
    res.clearCookie('username');
    // Redirecting to the /hello route
    res.redirect('/hello')
});


// Exporting this router file

module.exports = router;