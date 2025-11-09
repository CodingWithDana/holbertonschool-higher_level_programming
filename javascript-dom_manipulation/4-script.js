// Write a JavaScript script that adds a li element to a list
//  when the user clicks on the element with id add_item

// The new element must be: <li>Item</li> 
// The new element must be added to the ul element with class my_list

const triggerElement = document.querySelector('#add_item');
const listElement = document.querySelector('ul.my_list');

triggerElement.addEventListener('click', () => {
    if(listElement.classList.contains('my_list')) {
        const newElement = document.createElement('li');
        newElement.textContent = 'Item';
        listElement.appendChild(newElement);
    }
});