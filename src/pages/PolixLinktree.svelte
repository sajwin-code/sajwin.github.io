<script>
  import { theme, toggleTheme } from '../stores/theme.js';
  import { personalInfo } from '../data/portfolioData.js';
  import { navigate } from '../stores/router.js';
  import { showToast } from '../stores/toast.js';

  let isCardFlipped = false;

  function toggleCard() {
    isCardFlipped = !isCardFlipped;
  }
</script>

<div class="polix-page">
  <div class="polix-container">
    
    <header class="polix-header">
      <button class="nav-back-pill" on:click={() => navigate('/linktree')}>
        <i class="fas fa-arrow-left"></i> All Links
      </button>

      <div class="header-actions">
        <button class="nav-back-pill" on:click={() => navigate('/')}>
          <i class="fas fa-globe"></i> sajwin.dev
        </button>
        <button class="theme-toggle-mini" on:click={toggleTheme} aria-label="Toggle Theme">
          <i class={$theme === 'light' ? 'fas fa-moon' : 'fas fa-sun'}></i>
        </button>
      </div>
    </header>

    <!-- PoliX Branding Header -->
    <div class="brand-hero-box glass-card">
      <div class="polix-logo-wrapper">
        <img src="/images/polix/polix_logo.png" alt="PoliX Logo" class="polix-brand-logo" />
      </div>
      <p class="brand-tagline">Custom Websites • Business Solutions</p>
      <div class="founder-badge">
        <i class="fas fa-code"></i> Founded & Engineered by <strong>Sajwin Shakkeer Bin Jaffar</strong>
      </div>
    </div>

    <!-- Interactive 3D Business Card Showcase -->
    <div class="business-card-section">
      <div class="section-label-row">
        <span class="card-section-label"><i class="fas fa-id-card"></i> Official Business Card</span>
        <button class="flip-hint-btn" on:click={toggleCard}>
          <i class="fas fa-sync-alt"></i> {isCardFlipped ? 'View Front' : 'Flip to Back'}
        </button>
      </div>

      <div class="card-perspective-container" on:click={toggleCard} role="button" tabindex="0" on:keydown={(e) => e.key === 'Enter' && toggleCard()} aria-label="Interactive Business Card">
        <div class="card-3d-wrapper" class:flipped={isCardFlipped}>
          
          <!-- Card Front -->
          <div class="card-face card-front">
            <div class="card-inner-front">
              <div class="card-front-logo-wrap">
                <img src="/images/polix/polix_icon.png" alt="PoliX Asterisk" class="card-asterisk-icon" />
                <img src="/images/polix/polix_wordmark.png" alt="PoliX" class="card-wordmark-img" />
              </div>
              <p class="card-tagline-text">Custom Websites • Business Solutions</p>
              <div class="card-flip-prompt">
                <span>Tap or Click to Flip</span> <i class="fas fa-redo-alt"></i>
              </div>
            </div>
          </div>

          <!-- Card Back -->
          <div class="card-face card-back">
            <div class="card-inner-back">
              <div class="card-back-left">
                <h3 class="card-founder-name">SAJWIN SHAKKEER BIN JAFFAR</h3>
                <div class="card-founder-role">FOUNDER / WEB DEVELOPER</div>

                <div class="card-contact-rows">
                  <div class="card-row">
                    <i class="fas fa-phone-alt"></i>
                    <span>+91 9496 908 306</span>
                  </div>
                  <div class="card-row">
                    <i class="fas fa-envelope"></i>
                    <span>sajwinshakkeer@gmail.com</span>
                  </div>
                  <div class="card-row">
                    <i class="fas fa-globe"></i>
                    <span>sajwin.dev</span>
                  </div>
                  <div class="card-row">
                    <i class="fab fa-linkedin"></i>
                    <span>Linkedin / sajwin</span>
                  </div>
                </div>
              </div>

              <div class="card-back-right">
                <div class="qr-mockup-frame">
                  <div class="qr-code-graphic">
                    <i class="fas fa-qrcode qr-icon"></i>
                    <img src="/images/polix/polix_icon.png" alt="PoliX" class="qr-center-logo" />
                  </div>
                  <span class="qr-label">PoliX</span>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- PoliX Demo & Service Links -->
    <div class="links-list">
      <div class="links-group-title">PoliX Services & Solutions</div>

      <!-- 1. Full-Stack Portfolio -->
      <a href="/" class="link-card" on:click|preventDefault={() => navigate('/')}>
        <div class="link-icon-box polix-blue-box">
          <i class="fas fa-laptop-code"></i>
        </div>
        <div class="link-content">
          <div class="link-title-row">
            <span class="link-title">Full-Stack Solutions Portfolio</span>
            <span class="link-tag-pill">sajwin.dev</span>
          </div>
          <span class="link-sub">Explore production Django, Svelte & PostgreSQL architectures</span>
        </div>
        <i class="fas fa-arrow-right link-arrow"></i>
      </a>

      <!-- 2. Polix E-Commerce Platform -->
      <a href="https://github.com/sajwin-code/polix" target="_blank" rel="noopener noreferrer" class="link-card">
        <div class="link-icon-box polix-blue-box">
          <i class="fas fa-shopping-bag"></i>
        </div>
        <div class="link-content">
          <div class="link-title-row">
            <span class="link-title">Polix E-Commerce Engine Demo</span>
            <span class="link-tag-pill highlight">Live Demo</span>
          </div>
          <span class="link-sub">Complete production store with cart, checkout & catalog</span>
        </div>
        <i class="fas fa-external-link-alt link-arrow"></i>
      </a>

      <!-- 3. Start Project on WhatsApp -->
      <a href="https://wa.me/919496908306?text=Hi%20Sajwin,%20I'm%20interested%20in%20building%20a%20website%20with%20PoliX" target="_blank" rel="noopener noreferrer" class="link-card featured-link">
        <div class="link-icon-box whatsapp-box">
          <i class="fab fa-whatsapp"></i>
        </div>
        <div class="link-content">
          <div class="link-title-row">
            <span class="link-title">Start a Project on WhatsApp</span>
            <span class="link-tag-pill highlight">Quick Quote</span>
          </div>
          <span class="link-sub">Chat directly with the founder for instant quotes & timelines</span>
        </div>
        <i class="fas fa-bolt link-arrow" style="color: #25d366;"></i>
      </a>

      <!-- 4. Fiverr Escrow Orders -->
      <a href={personalInfo.fiverr} target="_blank" rel="noopener noreferrer" class="link-card">
        <div class="link-icon-box fiverr-box">
          <span style="font-weight: 900; font-size: 1.1rem;">fi</span>
        </div>
        <div class="link-content">
          <div class="link-title-row">
            <span class="link-title">Order via Fiverr Escrow Protection</span>
            <span class="link-tag-pill">Buyer Protected</span>
          </div>
          <span class="link-sub">Transparent tiers starting at $80 / ₹6,999</span>
        </div>
        <i class="fas fa-shield-alt link-arrow"></i>
      </a>

      <!-- 5. Direct Email Inquiry -->
      <a href="mailto:sajwinshakkeer@gmail.com?subject=PoliX%20Project%20Inquiry%20-%20Custom%20Website" class="link-card">
        <div class="link-icon-box">
          <i class="fas fa-envelope-open-text"></i>
        </div>
        <div class="link-content">
          <div class="link-title-row">
            <span class="link-title">Send Project Scope & RFP</span>
            <span class="link-tag-pill">Email</span>
          </div>
          <span class="link-sub">sajwinshakkeer@gmail.com</span>
        </div>
        <i class="fas fa-paper-plane link-arrow"></i>
      </a>

      <!-- 6. Direct Phone Call -->
      <a href="tel:+919496908306" class="link-card">
        <div class="link-icon-box">
          <i class="fas fa-phone-alt"></i>
        </div>
        <div class="link-content">
          <div class="link-title-row">
            <span class="link-title">Call Founder Direct</span>
            <span class="link-tag-pill">+91 9496 908 306</span>
          </div>
          <span class="link-sub">Consultation for custom business requirements</span>
        </div>
        <i class="fas fa-phone link-arrow"></i>
      </a>
    </div>

    <!-- Footer -->
    <footer class="polix-footer">
      <p class="footer-copy">
        &copy; 2026 PoliX • Custom Websites & Business Solutions • By <a href="/" on:click|preventDefault={() => navigate('/')}>Sajwin Shakkeer</a>
      </p>
    </footer>

  </div>
</div>

<style>
  .polix-page {
    min-height: 100vh;
    background: var(--bg-main);
    color: var(--text-primary);
    padding: 2rem 1rem 3rem 1rem;
    display: flex;
    justify-content: center;
    background-image: 
      radial-gradient(circle at 15% 15%, rgba(46, 91, 158, 0.12) 0%, transparent 40%),
      radial-gradient(circle at 85% 85%, rgba(56, 189, 248, 0.08) 0%, transparent 40%);
  }

  .polix-container {
    width: 100%;
    max-width: 640px;
    display: flex;
    flex-direction: column;
    gap: 1.75rem;
  }

  .polix-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .header-actions {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .nav-back-pill {
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

  .nav-back-pill:hover {
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

  .brand-hero-box {
    text-align: center;
    padding: 2.25rem 1.5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.75rem;
    border-color: rgba(46, 91, 158, 0.25);
    background: linear-gradient(135deg, rgba(46, 91, 158, 0.08), rgba(15, 23, 42, 0.6));
  }

  .polix-logo-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 0.25rem;
  }

  .polix-brand-logo {
    max-height: 70px;
    width: auto;
    object-fit: contain;
    filter: drop-shadow(0 4px 12px rgba(46, 91, 158, 0.25));
  }

  .brand-tagline {
    font-size: 1.05rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: var(--text-primary);
  }

  .founder-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.35rem 0.85rem;
    background: var(--bg-main);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-full);
    font-size: 0.78rem;
    color: var(--text-secondary);
  }

  .founder-badge strong {
    color: var(--text-primary);
  }

  /* Business Card 3D Flip Styles */
  .business-card-section {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }

  .section-label-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .card-section-label {
    font-size: 0.82rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--text-muted);
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .flip-hint-btn {
    background: transparent;
    border: none;
    color: var(--primary);
    font-size: 0.82rem;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }

  .card-perspective-container {
    perspective: 1000px;
    cursor: pointer;
    user-select: none;
  }

  .card-3d-wrapper {
    position: relative;
    width: 100%;
    min-height: 250px;
    transition: transform 0.7s cubic-bezier(0.4, 0, 0.2, 1);
    transform-style: preserve-3d;
  }

  .card-3d-wrapper.flipped {
    transform: rotateY(180deg);
  }

  .card-face {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
    border-radius: var(--radius-lg);
    overflow: hidden;
    box-shadow: var(--shadow-lg);
    border: 1px solid rgba(255, 255, 255, 0.15);
  }

  /* Card Front Design (Refined from uploaded media) */
  .card-front {
    background: #ffffff;
    color: #1b2838;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .card-inner-front {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2.5rem 1.5rem;
    text-align: center;
    gap: 1rem;
    width: 100%;
  }

  .card-front-logo-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.6rem;
  }

  .card-asterisk-icon {
    width: 48px;
    height: 48px;
    object-fit: contain;
  }

  .card-wordmark-img {
    height: 42px;
    width: auto;
    object-fit: contain;
  }

  .card-tagline-text {
    font-size: 0.95rem;
    font-weight: 700;
    color: #1b2838;
    letter-spacing: -0.01em;
  }

  .card-flip-prompt {
    font-size: 0.75rem;
    color: #64748b;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    margin-top: 0.5rem;
  }

  /* Card Back Design (Refined from uploaded media) */
  .card-back {
    background: #ffffff;
    color: #1b2838;
    transform: rotateY(180deg);
    display: flex;
    align-items: center;
  }

  .card-inner-back {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2rem 2.25rem;
    width: 100%;
    gap: 1.5rem;
  }

  .card-back-left {
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
  }

  .card-founder-name {
    font-family: var(--font-heading);
    font-size: 1.15rem;
    font-weight: 900;
    letter-spacing: 0.5px;
    color: #14213d;
    line-height: 1.2;
  }

  .card-founder-role {
    font-size: 0.8rem;
    font-weight: 800;
    letter-spacing: 1px;
    color: #14213d;
    margin-bottom: 0.6rem;
  }

  .card-contact-rows {
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
  }

  .card-row {
    display: flex;
    align-items: center;
    gap: 0.65rem;
    font-size: 0.85rem;
    font-weight: 700;
    color: #14213d;
  }

  .card-row i {
    width: 16px;
    color: #14213d;
    font-size: 0.85rem;
  }

  .card-back-right {
    display: flex;
    flex-direction: column;
    align-items: center;
    flex-shrink: 0;
  }

  .qr-mockup-frame {
    border: 2px solid #14213d;
    border-radius: 12px;
    padding: 0.75rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.25rem;
    background: #ffffff;
  }

  .qr-code-graphic {
    position: relative;
    width: 72px;
    height: 72px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .qr-icon {
    font-size: 70px;
    color: #14213d;
  }

  .qr-center-logo {
    position: absolute;
    width: 22px;
    height: 22px;
    background: #ffffff;
    padding: 2px;
    border-radius: 4px;
  }

  .qr-label {
    font-family: var(--font-heading);
    font-size: 0.95rem;
    font-weight: 900;
    color: #14213d;
    letter-spacing: 0.5px;
  }

  /* Links List */
  .links-group-title {
    font-size: 0.85rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--text-muted);
    margin-top: 0.5rem;
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
    border-color: rgba(46, 91, 158, 0.4);
    background: var(--bg-card-hover);
    box-shadow: var(--shadow-md);
  }

  .featured-link {
    border-color: rgba(46, 91, 158, 0.35);
    background: linear-gradient(135deg, rgba(46, 91, 158, 0.12), rgba(15, 23, 42, 0.4));
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

  .polix-blue-box {
    background: #2e5b9e;
    color: #ffffff;
  }

  .whatsapp-box {
    background: rgba(37, 211, 102, 0.15);
    color: #25d366;
  }

  .fiverr-box {
    background: rgba(16, 185, 129, 0.15);
    color: #10b981;
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
    background: rgba(46, 91, 158, 0.18);
    color: #38bdf8;
    border-color: rgba(46, 91, 158, 0.35);
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

  .polix-footer {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 1rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--border-color);
  }

  .footer-copy {
    font-size: 0.82rem;
    color: var(--text-muted);
    text-align: center;
  }

  .footer-copy a {
    color: var(--primary);
    text-decoration: none;
  }

  @media (max-width: 480px) {
    .card-inner-back {
      padding: 1.25rem 1rem;
      gap: 0.75rem;
    }
    .card-founder-name {
      font-size: 0.95rem;
    }
    .card-row {
      font-size: 0.75rem;
    }
    .qr-icon {
      font-size: 50px;
    }
    .qr-code-graphic {
      width: 52px;
      height: 52px;
    }
  }
</style>\n