<script>
  import { personalInfo } from '../data/portfolioData.js';
</script>

<footer class="footer">
  <div class="container">
    <div class="footer-top">
      <div>
        <a href="#home" class="nav-logo" aria-label="Sajwin Shakkeer - Full-Stack Developer">
          <span class="logo-icon-wrap"><i class="fas fa-code"></i></span>
          <span class="logo-text">Sajwin<span class="logo-domain">.dev</span></span>
        </a>
        <p style="color: var(--text-secondary); font-size: 0.9rem; margin-top: 0.5rem; max-width: 320px;">
          Full-Stack Web Developer, Python Specialist & Multilingual Creator.
        </p>
      </div>

      <div class="hero-socials">
        <a href={personalInfo.github} target="_blank" rel="noopener noreferrer" class="social-icon-btn" aria-label="GitHub">
          <i class="fab fa-github"></i>
        </a>
        <a href={personalInfo.fiverr} target="_blank" rel="noopener noreferrer" class="social-icon-btn" aria-label="Fiverr" title="Fiverr">
          <span style="font-weight: 900; font-size: 1rem;">fi</span>
        </a>
        <a href={personalInfo.linkedin} target="_blank" rel="noopener noreferrer" class="social-icon-btn" aria-label="LinkedIn">
          <i class="fab fa-linkedin-in"></i>
        </a>
        <a href="mailto:{personalInfo.email}" class="social-icon-btn" aria-label="Email">
          <i class="fas fa-envelope"></i>
        </a>
        <a href={personalInfo.whatsapp} target="_blank" rel="noopener noreferrer" class="social-icon-btn" aria-label="WhatsApp">
          <i class="fab fa-whatsapp"></i>
        </a>
      </div>
    </div>

    <div class="footer-bottom">
      <div>
        &copy; 2026 {personalInfo.name}. All rights reserved.
      </div>
      <div>
        Engineered with <i class="fas fa-heart" style="color: #ef4444;"></i> using Svelte 5, Python, Django & Vite.
      </div>
    </div>
  </div>
</footer>
