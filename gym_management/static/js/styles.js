// static/js/styles.js

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Toggle mobile navigation menu
const navbarToggler = document.querySelector('.navbar-toggler');
const navbarCollapse = document.querySelector('.navbar-collapse');

navbarToggler.addEventListener('click', () => {
    navbarCollapse.classList.toggle('show');
});

// Add hover effects to cards
const cards = document.querySelectorAll('.card');
cards.forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.style.transform = 'scale(1.05)';
        card.style.transition = 'transform 0.3s ease';
    });
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'scale(1)';
    });
});

// Form validation for the "Book a Demo" form
const demoForm = document.querySelector('#demo-form');
if (demoForm) {
    demoForm.addEventListener('submit', (e) => {
        const name = demoForm.querySelector('#name').value.trim();
        const email = demoForm.querySelector('#email').value.trim();
        const phone = demoForm.querySelector('#phone').value.trim();
        const gymName = demoForm.querySelector('#gym-name').value.trim();
        const date = demoForm.querySelector('#date').value.trim();
        const time = demoForm.querySelector('#time').value.trim();

        if (!name || !email || !phone || !gymName || !date || !time) {
            e.preventDefault();
            alert('Please fill out all fields.');
        }
    });
}

// Dark mode toggle (optional)
const darkModeToggle = document.querySelector('#dark-mode-toggle');
if (darkModeToggle) {
    darkModeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
    });

    // Check for saved dark mode preference
    if (localStorage.getItem('darkMode') === 'true') {
        document.body.classList.add('dark-mode');
    }
}