// App JavaScript
// This file contains JavaScript code for handling the sidebar toggle functionality 
// and any other interactive features of the application.
// static/js/app.js

document.addEventListener("DOMContentLoaded", function () {

    const toggle = document.getElementById("toggleSidebar");
    const sidebar = document.getElementById("sidebar");
    const content = document.getElementById("contentWrapper");
    const footer = document.getElementById("footer");

    toggle.addEventListener("click", function(){

        sidebar.classList.toggle("collapsed");
        content.classList.toggle("expanded");
        footer.classList.toggle("expanded");

    });

});