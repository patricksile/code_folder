const express = require('express');
const router = express.Router();
// requiring the data flashcardData file
const { data } = require('../data/flashcardData.json');
const { cards } = data;

// Randomize cards
router.get('/', (req, res) => {

    const numberOfCards = cards.length;
    const flashcardId = Math.floor(Math.random() * numberOfCards);
    res.redirect(`/cards/${flashcardId}`);
})
// Creating the /cards route and serving the card.pug template
router.get('/:id', (req, res) => {
    
    const { side } = req.query;
    const { id } = req.params;

    // redirecting to a question page in case we don't have a req.query (side)
    
    if ( !side ) {

        res.redirect(`/cards/${id}?side=question`);
    }
    
    const text = cards[id][side]; 
    const { hint } = cards[id]; // equivalent to const hint = cards[id].hint
    
    const templateData = { id, text};
    
    // Changing the Answer and Question logic
    
    if (side === 'question') {
        // Sets hint property in templateData object to hint object etc...
        templateData.hint = hint;
        templateData.sideToShow = 'answer';
        templateData.sideToShowDisplay = 'Answer';
    } else if (side === 'answer') {

        templateData.sideToShow = 'question';
        templateData.sideToShowDisplay = 'Question';
    }
    // console.log(req.query);

    // Rendering data(card.pug) to the client
    res.render('card', templateData);
});

module.exports = router;