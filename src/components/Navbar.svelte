<script>
  import { onMount } from 'svelte';
  import { theme, toggleTheme } from '../stores/theme.js';
  import { personalInfo } from '../data/portfolioData.js';

  let isScrolled = false;
  let isMobileOpen = false;
  let activeSection = 'home';

  const navLinks = [
    { href: '#about', label: 'About' },
    { href: '#languages', label: 'Languages' },
    { href: '#projects', label: 'Projects' },
    { href: '#pricing', label: 'Pricing' },
    { href: '#contact', label: 'Contact' }
  ];

  function handleScroll() {
    const scrollY = window.pageYOffset;
    isScrolled = scrollY > 50;

    const sections = document.querySelectorAll('section[id]');
    sections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - 120;
      const sectionId = current.getAttribute('id');
      if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
        activeSection = sectionId;
      }
    });
  }

  function toggleMobile() { isMobileOpen = !isMobileOpen; }
  function closeMobile() { isMobileOpen = false; }

  onMount(() => {
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  });
</script>

<header class="navbar" class:scrolled={isScrolled} id="navbar">
  <div class="container nav-container">
    <a href="#home" class="nav-logo" aria-label="Sajwin Shakkeer - Full-Stack Developer">
      <span class="logo-icon-wrap"><i class="fas fa-code"></i></span>
      <span class="logo-text">Sajwin<span class="logo-domain">.dev</span></span>
    </a>

    <nav class="nav-links">
      {#each navLinks as link}
        <a 
          href={link.href} 
          class="nav-link" 
          class:active={activeSection === link.href.substring(1)}
        >
          {link.label}
        </a>
      {/each}
    </nav>

    <div class="nav-actions">
      <button class="theme-toggle" on:click={toggleTheme} aria-label="Toggle Dark/Light Theme">
        <i class={$theme === 'light' ? 'fas fa-moon' : 'fas fa-sun'}></i>
      </button>

      <a href={personalInfo.fiverr} target="_blank" rel="noopener noreferrer" class="btn-fiverr-nav" title="Hire on Fiverr">
        <i class="fas fa-bolt"></i> Fiverr
      </a>

      <a href="#contact" class="btn-nav">
        <i class="fas fa-paper-plane"></i> Let's Talk
      </a>

      <button class="mobile-menu-btn" on:click={toggleMobile} aria-label="Toggle Menu">
        <i class={isMobileOpen ? 'fas fa-times' : 'fas fa-bars'}></i>
      </button>
    </div>
  </div>

  <div class="mobile-nav" class:open={isMobileOpen}>
    {#each navLinks as link}
      <a 
        href={link.href} 
        class="nav-link" 
        class:active={activeSection === link.href.substring(1)}
        on:click={closeMobile}
      >
        {link.label}
      </a>
    {/each}
    <a href={personalInfo.fiverr} target="_blank" rel="noopener noreferrer" class="btn-nav" style="margin-top: 0.5rem; justify-content: center;">
      <i class="fas fa-bolt"></i> Fiverr Profile (@sajwin_sj)
    </a>
  </div>
</header>

<style>
  .btn-fiverr-nav {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.48rem 0.95rem;
    border-radius: var(--radius-full);
    font-size: 0.85rem;
    font-weight: 700;
    background: rgba(16, 185, 129, 0.15);
    color: #10b981;
    border: 1px solid rgba(16, 185, 129, 0.3);
    transition: var(--transition);
  }
  .btn-fiverr-nav:hover {
    background: #10b981;
    color: #ffffff;
    box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35);
    transform: translateY(-2px);
  }
</style>
