// Write a JavaScript script that toggles the class of the header element
//  when the user clicks on the tag id toggle_header:
// The header element must always have one class: red or green,
//  never both in the same time and never empty. If the current
//  class is red, when the user click on id toggle_header element,
//  the class must be updated to green ; and the reverse.

const triggerElement = document.querySelector('#toggle_header');
const headerColor = document.querySelector('header');

triggerElement.addEventListener('click', () => {
    if (headerColor.classList.contains('green')){
        headerColor.classList.remove('green');
        headerColor.classList.add('red');
    } else {
        headerColor.classList.remove('red');
        headerColor.classList.add('green');
    }
});