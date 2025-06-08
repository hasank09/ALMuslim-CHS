
document.addEventListener('DOMContentLoaded', function() {
    // Filter buttons functionality
    const filterButtons = document.querySelectorAll('[data-filter]');
    const notices = document.querySelectorAll('.notice-card');

    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            button.classList.add('active');

            const filter = button.getAttribute('data-filter');

            notices.forEach(notice => {
                const category = notice.getAttribute('data-category');
                const noticeCol = notice.closest('.col-md-6');

                if (filter === 'all' || filter === category) {
                    noticeCol.style.display = 'block';
                } else {
                    noticeCol.style.display = 'none';
                }
            });
        });
    });

    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Legal matters filter functionality
    const legalFilterButtons = document.querySelectorAll('[data-legal-filter]');
    const legalCards = document.querySelectorAll('.legal-card');

    legalFilterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove active class from all buttons
            legalFilterButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            button.classList.add('active');

            const filter = button.getAttribute('data-legal-filter');

            legalCards.forEach(card => {
                const category = card.getAttribute('data-legal-category');
                const cardCol = card.closest('.col-md-6');

                if (filter === 'all' || filter === category) {
                    cardCol.style.display = 'block';
                } else {
                    cardCol.style.display = 'none';
                }
            });
        });
    });
});