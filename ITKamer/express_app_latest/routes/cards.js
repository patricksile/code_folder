const express = require('express');
const router = express.Router(); 
// requiring the data file flashcardData.json
const { data } = require('../data/flashcardData.json'); 
const { cards } = data; // ES6 equivalent of data.cards

// cards route
router.get('/', (req, res) => {
    // number of cards
    const numberOfCards = cards.length;
    // flashcardId number
    var flashcardId = Math.floor(Math.random() * numberOfCards);
    // redirecting to random id's
    res.redirect(`/cards/${flashcardId}`)
});

// card route or endpoint with parameter id
router.get('/:id', (req, res) => {
    // username cookies information(s)
    const name = req.cookies.username;
    const { side } = req.query;
    const { id } = req.params;
    if ( !side ) {
        // redirecting to the id card question
        return res.redirect(`/cards/${id}?side=question`);

    } 
    const { hint } = cards[id];
    const text = cards[id][side];
    const templateData = {id, name, text};

    if ( side === 'question') {
        templateData.hint  = hint;
        templateData.sideToShow = 'answer';
        templateData.sideToShowDisplay = 'Answer'; 
    } else if ( side === 'answer' ) {
        templateData.sideToShow = 'question';
        templateData.sideToShowDisplay = 'Question';
    } 

    // render the card page
    // console.log( req.query, req.params)
    res.render('card', templateData );
});
// exporting the router object
module.exports = router;