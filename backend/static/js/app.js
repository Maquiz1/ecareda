// App JavaScript
// This file contains JavaScript code for handling the sidebar toggle functionality 
// and any other interactive features of the application.
// static/js/app.js

document.addEventListener("DOMContentLoaded", function () {

    const toggle = document.getElementById("toggleSidebar");
    const sidebar = document.getElementById("sidebar");

    if (toggle && sidebar) {
        toggle.addEventListener("click", function(){
            if (window.innerWidth < 768) {
                sidebar.classList.toggle("show");
            } else {
                sidebar.classList.toggle("collapsed");
            }
        });
    }

    document.querySelectorAll(".menu-title").forEach(el => {
        el.addEventListener("click", function () {
            const icon = this.querySelector(".fa-chevron-down");
            if (icon) {
                icon.classList.toggle("fa-rotate-180");
            }
        });
    });

});