import { renderSidebar } from './Sidebar.js';

export function renderLayout(parentElement) {
    // Container
    const container = document.createElement('div');
    container.className = 'layout-container';

    // Sidebar
    const sidebar = renderSidebar();

    // Main Content
    const main = document.createElement('main');
    main.id = 'main-content';
    main.className = 'main-content';

    container.appendChild(sidebar);
    container.appendChild(main);

    parentElement.appendChild(container); // Mount to #app
}
