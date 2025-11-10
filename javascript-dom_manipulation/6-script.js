// Write a JavaScript script that fetches the character 'name'
// from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
// The name must be displayed in the HTML tag with id character
// You must use the Fetch API

const tagElement = document.getElementById('character');

fetch ('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => {
        if (response.ok) {
            return response.json();
        }
    })
    .then(data => {
        tagElement.textContent = data.name;
    });