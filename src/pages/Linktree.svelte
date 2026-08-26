<script>
  import { theme, toggleTheme } from '../stores/theme.js';
  import { personalInfo } from '../data/portfolioData.js';
  import { navigate } from '../stores/router.js';
  import { showToast } from '../stores/toast.js';
</script>

<div class="linktree-page">
  <div class="linktree-container">
    
    <header class="linktree-header">
      <button class="back-home-btn" on:click={() => navigate('/')}>
        <i class="fas fa-arrow-left"></i> sajwin.dev
      </button>

      <button class="theme-toggle-mini" on:click={toggleTheme} aria-label="Toggle Theme">
        <i class={$theme === 'light' ? 'fas fa-moon' : 'fas fa-sun'}></i>
      </button>
    </header>

    <div class="profile-card">
      <div class="avatar-wrapper">
        <img src={personalInfo.avatar} alt={personalInfo.name} class="profile-avatar" />
        <span class="online-indicator" title="Available for Projects"></span>
      </div>

      <h1 class="profile-name">{personalInfo.name}</h1>
      <p class="profile-tagline">Full-Stack Developer • Python/Django • Polyglot</p>
      
      <div class="profile-badges">
        <span class="mini-chip"><i class="fas fa-map-marker-alt"></i> Kannur, India</span>
        <span class="mini-chip"><i class="fas fa-globe"></i> 7 Languages</span>
        <span class="mini-chip"><i class="fas fa-graduation-cap"></i> BCA @ MUJ</span>
      </div>
    </div>

    <!-- Links List -->
    <div class="links-list">
      
      <!-- PoliX Initiative Feature Link -->
      <a href="/linktree/polix" class="link-card featured-link" on:click|preventDefault={() => navigate('/linktree/polix')}>
        <div class="link-icon-box polix-icon-box">
          <i class="fas fa-asterisk"></i>
        </div>
        <div class="link-content">
          <div class="link-title-row">
            <span class="link-title">PoliX Business Solutions</span>
            <span class="link-tag-pill highlight">Freelance Agency</span>
          </div>
          <span class="link-sub">Custom Websites & Digital Solutions for Businesses</span>
        </div>
        <i class="fas fa-chevron-right link-arrow"></i>
      </a>

      <!-- Portfolio -->
      <a href="/" class="link-card" on:click|preventDefault={() => navigate('/')}>
        <div class="link-icon-box">
          <i class="fas fa-laptop-code"></i>
        </div>
        <div class="link-content">
          <div class="link-title-row">
            <span class="link-title">Official Portfolio Website</span>
            <span class="link-tag-pill">sajwin.dev</span>
          </div>
          <span class="link-sub">Interactive 3D Globe, Full Stack Work & Capabilities</span>
        </div>
        <i class="fas fa-chevron-right link-arrow"></i>
      </a>

      <!-- Fiverr -->
      <a href={personalInfo.fiverr} target="_blank" rel="noopener noreferrer" class="link-card">
        <div class="link-icon-box fiverr-box">
          <span style="font-weight: 900; font-size: 1.1rem;">fi</span>
        </div>
        <div class="link-content">
          <div class="link-title-row">
            <span class="link-title">Order on Fiverr</span>
            <span class="link-tag-pill">@sajwin_sj</span>
          </div>
          <span class="link-sub">Escrow Protected Freelance Development Tiers</span>
        </div>
        <i class="fas fa-external-link-alt link-arrow"></i>
      </a>

      <!-- GitHub -->
      <a href={personalInfo.github} target="_blank" rel="noopener noreferrer" class="link-card">
        <div class="link-icon-box">
          <i class="fab fa-github"></i>
        </div>
        <div class="link-content">
          <div class="link-title-row">
            <span class="link-title">GitHub Repositories</span>
            <span class="link-tag-pill">@sajwin-code</span>
          </div>
          <span class="link-sub">Polix E-Commerce, Syncora Social & Open-Source Code</span>
        </div>
        <i class="fas fa-external-link-alt link-arrow"></i>
      </a>

      <!-- LinkedIn -->
      <a href={personalInfo.linkedin} target="_blank" rel="noopener noreferrer" class="link-card">
        <div class="link-icon-box">
          <i class="fab fa-linkedin-in"></i>
        </div>
        <div class="link-content">
          <div class="link-title-row">
            <span class="link-title">LinkedIn Profile</span>
            <span class="link-tag-pill">sajwin</span>
          </div>
          <span class="link-sub">Professional Network & Academic Updates</span>
        </div>
        <i class="fas fa-external-link-alt link-arrow"></i>
      </a>

      <!-- WhatsApp -->
      <a href={personalInfo.whatsapp} target="_blank" rel="noopener noreferrer" class="link-card">
        <div class="link-icon-box whatsapp-box">
          <i class="fab fa-whatsapp"></i>
        </div>
        <div class="link-content">
          <div class="link-title-row">
            <span class="link-title">WhatsApp Direct Chat</span>
            <span class="link-tag-pill">+91 9496 908 306</span>
          </div>
          <span class="link-sub">Instant Chat for Projects & Queries</span>
        </div>
        <i class="fas fa-external-link-alt link-arrow"></i>
      </a>

      <!-- Email -->
      <a href="mailto:{personalInfo.email}" class="link-card">
        <div class="link-icon-box">
          <i class="fas fa-envelope"></i>
        </div>
        <div class="link-content">
          <div class="link-title-row">
            <span class="link-title">Direct Email</span>
            <span class="link-tag-pill">sajwinshakkeer@gmail.com</span>
          </div>
          <span class="link-sub">Inquiries, Contracts & Collaboration</span>
        </div>
        <i class="fas fa-external-link-alt link-arrow"></i>
      </a>
    </div>

    <!-- Socials Footer -->
    <footer class="linktree-footer">
      <div class="linktree-social-row">
        <a href={personalInfo.github} target="_blank" rel="noopener noreferrer" class="social-circle" aria-label="GitHub"><i class="fab fa-github"></i></a>
        <a href={personalInfo.fiverr} target="_blank" rel="noopener noreferrer" class="social-circle" aria-label="Fiverr"><span style="font-weight: 900; font-size: 0.9rem;">fi</span></a>
        <a href={personalInfo.linkedin} target="_blank" rel="noopener noreferrer" class="social-circle" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
        <a href="mailto:{personalInfo.email}" class="social-circle" aria-label="Email"><i class="fas fa-envelope"></i></a>
        <a href={personalInfo.whatsapp} target="_blank" rel="noopener noreferrer" class="social-circle" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>
      </div>

      <p class="footer-copy">
        &copy; 2026 Sajwin Shakkeer Bin Jaffar • <a href="/" on:click|preventDefault={() => navigate('/')}>sajwin.dev</a>
      </p>
    </footer>

  </div>
</div>

<style>
  .linktree-page {
    min-height: 100vh;
    background: var(--bg-main);
    color: var(--text-primary);
    padding: 2rem 1rem 3rem 1rem;
    display: flex;
    justify-content: center;
    background-image: 
      radial-gradient(circle at 10% 20%, rgba(56, 189, 248, 0.06) 0%, transparent 40%),
      radial-gradient(circle at 90% 80%, rgba(45, 212, 191, 0.04) 0%, transparent 40%);
  }

  .linktree-container {
    width: 100%;
    max-width: 620px;
    display: flex;
    flex-direction: column;
    gap: 1.75rem;
  }

  .linktree-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .back-home-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.45rem 0.9rem;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-full);
    color: var(--text-secondary);
    font-size: 0.85rem;
    font-weight: 600;
    cursor: pointer;
    transition: var(--transition);
  }

  .back-home-btn:hover {
    color: var(--primary);
    border-color: var(--primary);
  }

  .theme-toggle-mini {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    color: var(--text-primary);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.95rem;
    transition: var(--transition);
  }

  .theme-toggle-mini:hover {
    color: var(--primary);
    border-color: var(--primary);
  }

  .profile-card {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.75rem;
  }

  .avatar-wrapper {
    position: relative;
    width: 96px;
    height: 96px;
  }

  .profile-avatar {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid var(--primary);
    box-shadow: 0 4px 20px var(--primary-glow);
  }

  .online-indicator {
    position: absolute;
    bottom: 4px;
    right: 4px;
    width: 14px;
    height: 14px;
    background: #10b981;
    border-radius: 50%;
    border: 2px solid var(--bg-main);
    box-shadow: 0 0 8px #10b981;
  }

  .profile-name {
    font-family: var(--font-heading);
    font-size: 1.55rem;
    font-weight: 800;
    color: var(--text-primary);
    line-height: 1.2;
  }

  .profile-tagline {
    font-size: 0.92rem;
    color: var(--text-secondary);
    max-width: 440px;
  }

  .profile-badges {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.5rem;
    margin-top: 0.25rem;
  }

  .mini-chip {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.25rem 0.65rem;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-full);
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--text-secondary);
  }

  .mini-chip i {
    color: var(--primary);
  }

  .links-list {
    display: flex;
    flex-direction: column;
    gap: 0.85rem;
  }

  .link-card {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem 1.25rem;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    transition: var(--transition);
    text-decoration: none;
    color: inherit;
  }

  .link-card:hover {
    transform: translateY(-2px);
    border-color: var(--border-glow);
    background: var(--bg-card-hover);
    box-shadow: var(--shadow-md);
  }

  .featured-link {
    border-color: rgba(56, 189, 248, 0.35);
    background: linear-gradient(135deg, rgba(56, 189, 248, 0.08), rgba(45, 212, 191, 0.05));
  }

  .featured-link:hover {
    border-color: var(--primary);
    box-shadow: 0 4px 20px var(--primary-glow);
  }

  .link-icon-box {
    width: 44px;
    height: 44px;
    border-radius: var(--radius-md);
    background: rgba(56, 189, 248, 0.12);
    color: var(--primary);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.25rem;
    flex-shrink: 0;
  }

  .polix-icon-box {
    background: #2e5b9e;
    color: #ffffff;
  }

  .fiverr-box {
    background: rgba(16, 185, 129, 0.15);
    color: #10b981;
  }

  .whatsapp-box {
    background: rgba(37, 211, 102, 0.15);
    color: #25d366;
  }

  .link-content {
    display: flex;
    flex-direction: column;
    gap: 0.15rem;
    flex-grow: 1;
    overflow: hidden;
  }

  .link-title-row {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex-wrap: wrap;
  }

  .link-title {
    font-size: 0.98rem;
    font-weight: 700;
    color: var(--text-primary);
  }

  .link-tag-pill {
    font-size: 0.7rem;
    font-weight: 700;
    padding: 0.15rem 0.5rem;
    border-radius: var(--radius-full);
    background: var(--bg-main);
    color: var(--text-muted);
    border: 1px solid var(--border-color);
  }

  .link-tag-pill.highlight {
    background: rgba(56, 189, 248, 0.15);
    color: var(--primary);
    border-color: rgba(56, 189, 248, 0.3);
  }

  .link-sub {
    font-size: 0.82rem;
    color: var(--text-secondary);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .link-arrow {
    color: var(--text-muted);
    font-size: 0.9rem;
    transition: var(--transition);
    flex-shrink: 0;
  }

  .link-card:hover .link-arrow {
    color: var(--primary);
    transform: translateX(3px);
  }

  .linktree-footer {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    margin-top: 1rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--border-color);
  }

  .linktree-social-row {
    display: flex;
    gap: 0.75rem;
  }

  .social-circle {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-secondary);
    font-size: 1.05rem;
    transition: var(--transition);
    text-decoration: none;
  }

  .social-circle:hover {
    color: var(--primary);
    border-color: var(--primary);
    transform: translateY(-2px);
  }

  .footer-copy {
    font-size: 0.82rem;
    color: var(--text-muted);
  }

  .footer-copy a {
    color: var(--primary);
    text-decoration: none;
  }
</style>\n