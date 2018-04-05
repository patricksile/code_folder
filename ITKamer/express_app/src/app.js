'use strict';
// Express module import.
var express = require('express'),
      posts = require('./mock/posts.json');
// Express object.
var app = express();

// Putting templates in use
app.set('view engine', 'jade');
app.set('views', __dirname + '/templates');

// debugger;
// Creating a route index('/')
app.get('/', function(req, res) {
    res.render('index');
});

// blog route ('/blog')
app.get('/blog/:title?', function(req, res) {
    var title = req.params.title;
    if (title === undefined) {
        res.status(503);
        res.send("This page is under construction!");
    } else {
        var post = posts[title] || {};
        res.render("post", { post: post});
    }
    var post = posts[title];
    res.send(post);
})
// Listening on port 3000.
app.listen(3000, function() {
    console.log("The frontend server is running on port 3000!")
});