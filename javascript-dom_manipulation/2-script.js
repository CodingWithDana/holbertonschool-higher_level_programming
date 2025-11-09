// Write a JavaScript script that adds the class red to the header element 
// when the user clicks on the tag with id red_header
const triggerElement = document.querySelector('#red_header');
const headerColor = document.querySelector('header');

triggerElement.addEventListener('click', () => {
    headerColor.classList.add('red');
})