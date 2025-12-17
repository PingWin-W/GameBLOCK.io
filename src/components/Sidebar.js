export function renderSidebar() {
  const aside = document.createElement('aside');
  aside.className = 'sidebar';

  // Basic styles inline for now, ideally in CSS
  // Using utility classes from style.css once added

  const template = `
    <div class="logo-area">
      <h1>Portal</h1>
    </div>
    
    <nav class="nav-menu">
      <a href="#/" class="nav-item active">
        <span class="icon">🏠</span>
        <span>Home</span>
      </a>
      <a href="#/popular" class="nav-item">
        <span class="icon">🔥</span>
        <span>Popular</span>
      </a>
      <a href="#/new" class="nav-item">
        <span class="icon">✨</span>
        <span>New</span>
      </a>
    </nav>
    
    <div class="nav-footer">
      <span class="version">v2.0</span>
    </div>
  `;

  aside.innerHTML = template;

  // Active State Logic
  const updateActiveState = () => {
    const hash = window.location.hash || '#/';
    const navItems = aside.querySelectorAll('.nav-item');

    navItems.forEach(item => {
      const href = item.getAttribute('href');
      if (href === hash) {
        item.classList.add('active');
      } else {
        item.classList.remove('active');
      }
    });
  };

  window.addEventListener('hashchange', updateActiveState);
  window.addEventListener('popstate', updateActiveState);

  // Initial check
  setTimeout(updateActiveState, 0);

  return aside;
}
