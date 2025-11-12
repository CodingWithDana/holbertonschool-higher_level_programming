// Write a JavaScript script that fetches from https://hellosalut.stefanbohacek.com/?lang=fr 
//    and displays the value of hello from that fetch in the HTML element with id 'hello'
// The translation of “hello” must be displayed in the HTML element with id hello
// Your script must work when it is imported from the <head> tag

document.addEventListener('DOMContentLoaded', () => {
    const idElement = document.getElementById('hello');
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
        .then(response => {
            if (response.ok) {
                return response.json();
            }
        })
        .then(data => {
            idElement.textContent = data.hello;
        });
});
