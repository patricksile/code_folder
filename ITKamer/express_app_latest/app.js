// Bringing in express Objects, Methods, and Properties.
const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');

// Central part of the application
const app = express();
// Mounting the bodyParser,cookie-parser... Middleware 
app.use(bodyParser.urlencoded({ extended: false}));
app.use(cookieParser());
// static file MiddleWare, routed at /static url
app.use('/static', express.static('public'));
// Setting up the vew engine that our app is going to use.
app.set('view engine','pug');

// Access to index.js in routes folder and use (middleware) it.
const mainRoutes = require('./routes');
const cardRoutes = require('./routes/cards');
app.use(mainRoutes);
app.use('/cards', cardRoutes);
// Middleware to handle error handler middleware
app.use((req, res, next) => {
    const err = new Error('Not Found');
    err.status = 404;
    next(err);
})
// Error handler middleware
app.use((err, req, res, next) => {
    res.locals.error = err; 
    res.status(err.status);
    res.render('error');
})
// Listening in the server 
app.listen(3000, () => {
    console.log("The application is running on localhost:3000!");
});