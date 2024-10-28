// script.js

//// Wait for the DOM to fully load before running the script
//document.addEventListener("DOMContentLoaded", function() {
//    // Grab the toggle button (you can create this as part of the navbar)
//    const toggleButton = document.createElement('button');
//    toggleButton.textContent = 'Toggle Light/Dark Mode';
//    toggleButton.style.marginLeft = '15px';
//
//    // Add the toggle button to the navbar
//    const navbar = document.querySelector('.navbar');
//    navbar.appendChild(toggleButton);
//
//    // Add event listener for theme toggle
//    toggleButton.addEventListener('click', function() {
//        document.body.classList.toggle('light-mode');
//    });
//});
//
//// Optional: Add functionality for the user to set theme preference to local storage
//if (localStorage.getItem('theme') === 'light') {
//    document.body.classList.add('light-mode');
//}
//
//// Save theme preference to local storage
//document.querySelector('button').addEventListener('click', function() {
//    if (document.body.classList.contains('light-mode')) {
//        localStorage.setItem('theme', 'light');
//    } else {
//        localStorage.removeItem('theme');
//    }
//});
//