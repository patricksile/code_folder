// const myHeading = document.getElementsByTagName("h1")[0];
// const myButton= document.getElementById("myButton");
// const myTextInput = document.getElementById("myTextInput");
// myButton.addEventListener('click', () => {
//     myHeading.style.color = myTextInput.value;
// });
const myList = document.getElementsByTagName('li');
for (let i = 0; i < myList.length; i += 1) {
    myList[i].style.color = 'purple';
}
const errorNotPurple = document.querySelectorAll('.error-not-purple');
for (let i = 0; i < errorNotPurple.length; i += 1) {
    errorNotPurple[i].style.color = 'red';
}
const evens = document.querySelectorAll('li:nth-child(odd)');
for (let i = 0; i < evens.length; i += 1) {
    evens[i].style.backgroundColor = 'lightgray';
}

// Third part 01 innerHTML and textContent

const descriptionInput = document.querySelector('input.description');
const descriptionP = document.querySelector('p.description');
const descriptionButton = document.querySelector('button.description');
const addItemInput = document.querySelector('input.addItemInput')
const addItemButton = document.querySelector('button.addItemButton')

descriptionButton.addEventListener('click', () => {
    // descriptiionP.textContent = input.value + ':';
    descriptionP.innerHTML = descriptionInput.value + ':';
});
// Third part 02 Element.attribute, Element.className
// p.title = "List description";
// Third part 03
// Lets hide the list
const toggleList = document.getElementById('toggleList');
const divList = document.querySelector('.list');
toggleList.addEventListener('click', () => {
    if (divList.style.display === 'none') {
        toggleList.textContent = "Hide list";
        divList.style.display = "block";
    } else {
        toggleList.textContent = "Show list";
        divList.style.display = "none"; 
    }
    // divList.style.display = "none";
})

// document.createElement();
addItemButton.addEventListener ('click', () => {
    let li = document.createElement('li');
    li.textContent = addItemInput.value;
    console.log(li);
})