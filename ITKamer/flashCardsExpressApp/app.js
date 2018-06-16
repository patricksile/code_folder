const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
// Express application
const app = express();

// MiddleWares
app.use(bodyParser.urlencoded({ extended:false}));
app.use(cookieParser());


// Set the app to use pug for templating
app.set('view engine', 'pug');

// MiddleWares


// Importing the router file

const mainRoutes = require('./routes')
const cardRoutes = require('./routes/cards'); // './routes/cards pointing to the cards.pug file

//
app.use(mainRoutes);
app.use('/cards', cardRoutes);


// Error handler

app.use((req, res, next) => {

    err = new Error('Not Found')
    err.status = 404;
    next(err);
})

app.use((err, req, res, next) => {
   
    res.locals.error = err;
    res.status(err.status);
    res.render('error'); // 'error' here is the name of the rendered file error.pug
    next();
});
// Development server on port 3000
app.listen(3000, () => {
    
    console.log("The application is running on port: 3000!")
});