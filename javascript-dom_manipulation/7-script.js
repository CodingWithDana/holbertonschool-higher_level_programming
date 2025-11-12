// Write a JavaScript script that fetches and lists the title
// for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

// All movie titles must be list in the HTML ul element with id list_movies
// You must use the Fetch API.

const idElement = document.getElementById('list_movies');

fetch ('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
        if (response.ok) {
            return response.json();
        }
    })
    .then(data => {
        data.results.forEach(films => {
            const newElement = document.createElement('li');
            newElement.textContent = films.title;
            idElement.appendChild(newElement);
        });
    });