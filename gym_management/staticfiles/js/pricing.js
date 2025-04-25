// Open modal when "Select Plan" is clicked
document.querySelectorAll('.btn-select-plan').forEach(button => {
    button.addEventListener('click', (e) => {
        e.preventDefault();
        const planCard = e.target.closest('.plan-card');
        if (planCard) {
            const planName = planCard.querySelector('h2').textContent;
            document.getElementById('selectedPlan').textContent = planName;
            document.getElementById('planModal').style.display = 'flex';
        }
    });
});

// Close modal
document.querySelector('.close-modal').addEventListener('click', () => {
    document.getElementById('planModal').style.display = 'none';
});

// Close modal when clicking outside
window.addEventListener('click', (e) => {
    if (e.target === document.getElementById('planModal')) {
        document.getElementById('planModal').style.display = 'none';
    }
});
