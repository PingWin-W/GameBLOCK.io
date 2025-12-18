import { renderHome } from './pages/Home.js';
import { renderPlayer } from './pages/Player.js';

const routes = {
    '/': renderHome,
    '/game': renderPlayer // /game?slug=...
};

export function initRouter() {
    window.addEventListener('popstate', handleLocation);
    handleLocation(); // Handle initial load
}

async function handleLocation() {
    window.scrollTo(0, 0);
    const path = window.location.pathname;
    const searchParams = new URLSearchParams(window.location.search);

    // Basic routing logic
    // If we are served from a subdirectory (e.g. /v2_rebuild/), we might need to handle base path.
    // For simplicity, we'll check query params or hash for now if pure static.
    // Let's use Hash-based routing for safest static deployment compatibility
    // or just check "current view" state managed by our own navigate function.

    // Actually, let's use a simple query-param based router or hash router to avoid server config issues.
    // Hash router is safer for GitHub Pages without SPA config.

    const hash = window.location.hash || '#/';

    // Parse hash: #/game/slug-name or #/
    const mainContent = document.getElementById('main-content');
    mainContent.innerHTML = ''; // Clear current view

    if (hash.startsWith('#/game/')) {
        const slug = hash.replace('#/game/', '');
        renderPlayer(mainContent, slug);
    } else {
        renderHome(mainContent);
    }
}

export function navigate(path) {
    window.history.pushState({}, "", path);
    handleLocation();
}
