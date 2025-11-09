// Write a JavaScript script that updates the text of the header element to New Header!!! 
// when the user clicks on the element with id update_header

const triggerElement = document.querySelector('#update_header');
const updateHeaderElement = document.querySelector('header');

triggerElement.addEventListener('click', () => {
    updateHeaderElement.textContent = 'New Header!!!';
});