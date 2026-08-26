<script>
  import { onMount } from 'svelte';
  import { personalInfo } from '../data/portfolioData.js';

  let currentText = '';
  let phraseIndex = 0;
  let charIndex = 0;
  let isDeleting = false;

  const phrases = personalInfo.roleTitles;

  function handleTyping() {
    const currentPhrase = phrases[phraseIndex];
    if (isDeleting) {
      currentText = currentPhrase.substring(0, charIndex - 1);
      charIndex--;
    } else {
      currentText = currentPhrase.substring(0, charIndex + 1);
      charIndex++;
    }

    let speed = isDeleting ? 45 : 85;

    if (!isDeleting && charIndex === currentPhrase.length) {
      speed = 2000;
      isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      phraseIndex = (phraseIndex + 1) % phrases.length;
      speed = 350;
    }

    setTimeout(handleTyping, speed);
  }

  onMount(() => {
    setTimeout(handleTyping, 600);
  });
</script>

<section class="hero" id="home">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-content">
        <div class="status-badge">
          <span class="pulse-dot"></span>
          Available for Freelance & Full-Time Roles
        </div>

        <h1 class="hero-title">
          Hi, I'm <span class="gradient-text">{personalInfo.shortName} Shakkeer</span><br>Bin Jaffar
        </h1>

        <div class="typing-wrapper">
          <span id="typing-text">{currentText}</span><span class="typing-cursor"></span>
        </div>

        <p class="hero-description">
          Full-Stack Developer and BCA scholar at <strong>Manipal University Jaipur</strong> with expertise in <strong>Python, Django, Svelte, PostgreSQL</strong>, and modern AI-driven engineering. Combining clean backend architecture with intuitive UI/UX and native multilingual proficiency.
        </p>

        <div class="hero-cta">
          <a href="#projects" class="btn btn-primary">
            <span>Explore Projects</span> <i class="fas fa-arrow-right"></i>
          </a>
          <a href="#contact" class="btn btn-outline">
            <i class="fas fa-envelope"></i> Get in Touch
          </a>
        </div>

        <div class="hero-socials">
          <a href={personalInfo.github} target="_blank" rel="noopener noreferrer" class="social-icon-btn" aria-label="GitHub Profile" title="GitHub">
            <i class="fab fa-github"></i>
          </a>
          <a href={personalInfo.fiverr} target="_blank" rel="noopener noreferrer" class="social-icon-btn" aria-label="Fiverr Profile" title="Fiverr">
            <span style="font-weight: 900; font-size: 0.95rem;">fi</span>
          </a>
          <a href={personalInfo.linkedin} target="_blank" rel="noopener noreferrer" class="social-icon-btn" aria-label="LinkedIn Profile" title="LinkedIn">
            <i class="fab fa-linkedin-in"></i>
          </a>
          <a href="mailto:{personalInfo.email}" class="social-icon-btn" aria-label="Email Me" title="Email">
            <i class="fas fa-envelope"></i>
          </a>
          <a href={personalInfo.whatsapp} target="_blank" rel="noopener noreferrer" class="social-icon-btn" aria-label="WhatsApp Contact" title="WhatsApp">
            <i class="fab fa-whatsapp"></i>
          </a>
        </div>
      </div>

      <div class="hero-media">
        <div class="hero-media-wrapper">
          <img src={personalInfo.avatar} alt="{personalInfo.name} - Full Stack Developer" class="hero-banner-img" />
        </div>
      </div>
    </div>
  </div>
</section>
