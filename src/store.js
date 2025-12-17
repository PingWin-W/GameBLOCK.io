// Simple centralized store
let games = [];

export async function fetchGames() {
    try {
        // Determine the environment (dev vs prod path)
        // For local dev without build, valid path depends on server root. 
        // Assuming server root is v2_rebuild/
        const response = await fetch('./src/data/games.json');

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        games = await response.json();
        console.log(`Loaded ${games.length} games`);
    } catch (e) {
        console.error("Could not fetch games.json", e);
        // Fallback or re-throw
        throw e;
    }
}

export function getAllGames() {
    return games;
}

export function getGameBySlug(slug) {
    return games.find(g => g.slug === slug);
}

export function searchGames(query) {
    if (!query) return games;
    const lowerQuery = query.toLowerCase();
    return games.filter(g => g.name.toLowerCase().includes(lowerQuery));
}
