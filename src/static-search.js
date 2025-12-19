/**
 * Static Search Functionality
 * Handles client-side filtering of pre-rendered game cards.
 * Replaces the heavy SPA logic for simple grid filtering.
 */

document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.querySelector('.search-bar input');

    // Only run if search input exists on this page
    if (!searchInput) return;

    const grid = document.querySelector('.games-grid');
    if (!grid) return;

    // Debounce function to prevent excessive calculations
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    const handleSearch = (e) => {
        const query = e.target.value.toLowerCase().trim();
        const cards = grid.querySelectorAll('.game-card');
        let hasResults = false;

        cards.forEach(card => {
            const titleElement = card.querySelector('h3');
            if (!titleElement) return;

            const name = titleElement.textContent.toLowerCase();

            if (name.includes(query)) {
                card.style.display = ''; // Reset to default (usually block or flex)
                // Optional: Add simple fade in if it was hidden
                if (card.style.display === 'none') {
                    card.style.animation = 'fadeIn 0.3s ease';
                }
                hasResults = true;
            } else {
                card.style.display = 'none';
            }
        });

        // Handle "No Results" message
        let noResultsMsg = grid.querySelector('.no-results');

        if (!hasResults) {
            if (!noResultsMsg) {
                noResultsMsg = document.createElement('div');
                noResultsMsg.className = 'no-results';
                noResultsMsg.style.gridColumn = '1 / -1';
                noResultsMsg.style.textAlign = 'center';
                noResultsMsg.style.padding = '2rem';
                noResultsMsg.style.color = 'var(--color-text-dim)';
                noResultsMsg.innerHTML = `<h3>No games found matching "${e.target.value}"</h3>`;
                grid.appendChild(noResultsMsg);
            } else {
                noResultsMsg.querySelector('h3').textContent = `No games found matching "${e.target.value}"`;
                noResultsMsg.style.display = 'block';
            }
        } else if (noResultsMsg) {
            noResultsMsg.style.display = 'none';
        }
    };

    searchInput.addEventListener('input', debounce(handleSearch, 150));

    // Prevent form submission if inside a form (though it's usually just an input)
    searchInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
        }
    });
});
