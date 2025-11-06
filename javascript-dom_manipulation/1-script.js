const selectTag = document.querySelector('#red_header');
const headerColor = document.querySelector('header');
selectTag.addEventListener('click', () => {
	headerColor.style.color = '#FF0000';
});