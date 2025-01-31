// Sélection des éléments de menu latéral
const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

allSideMenu.forEach(item => {
    const li = item.parentElement;
    item.addEventListener('click', function () {
        allSideMenu.forEach(i => {
            i.parentElement.classList.remove('active');
        });
        li.classList.add('active');
    });
});

// TOGGLE SIDEBAR
const menuBar = document.querySelector('#content nav .bx.bx-menu');
const sidebar = document.getElementById('sidebar');

menuBar.addEventListener('click', function () {
    sidebar.classList.toggle('hide');
});



// Gestion du mode sombre
const switchMode = document.getElementById('switch-mode');

// Charger l'état du mode sombre depuis localStorage au chargement de la page
document.addEventListener('DOMContentLoaded', () => {
    const darkMode = localStorage.getItem('darkMode');
    if (darkMode === 'enabled') {
        // Apply dark mode by setting CSS variables
        document.documentElement.style.setProperty('--light', '#0C0C1E');
        document.documentElement.style.setProperty('--grey', '#060714');
        document.documentElement.style.setProperty('--dark', '#FBFBFB');
        switchMode.checked = true;
    } else {
        // Apply light mode by resetting CSS variables
        document.documentElement.style.setProperty('--light', '#F9F9F9');
        document.documentElement.style.setProperty('--grey', '#eee');
        document.documentElement.style.setProperty('--dark', '#342E37');
        switchMode.checked = false;
    }
});

// Basculer le mode sombre et enregistrer dans localStorage
switchMode.addEventListener('change', function () {
    if (this.checked) {
        // Apply dark mode
        document.documentElement.style.setProperty('--light', '#0C0C1E');
        document.documentElement.style.setProperty('--grey', '#060714');
        document.documentElement.style.setProperty('--dark', '#FBFBFB');
        localStorage.setItem('darkMode', 'enabled'); // Enregistrer le mode sombre activé
    } else {
        // Apply light mode
        document.documentElement.style.setProperty('--light', '#F9F9F9');
        document.documentElement.style.setProperty('--grey', '#eee');
        document.documentElement.style.setProperty('--dark', '#342E37');
        localStorage.setItem('darkMode', 'disabled'); // Enregistrer le mode clair
    }
});

// Datatable
$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();

    var checkbox = $('table tbody input[type="checkbox"]');
    $("#selectAll").click(function () {
        if (this.checked) {
            checkbox.each(function () {
                this.checked = true;
            });
        } else {
            checkbox.each(function () {
                this.checked = false;
            });
        }
    });
    checkbox.click(function () {
        if (!this.checked) {
            $("#selectAll").prop("checked", false);
        }
    });
});