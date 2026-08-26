<script>
  import { personalInfo } from '../data/portfolioData.js';
</script>

<section class="about-section" id="about">
  <div class="container">
    <div class="section-header">
      <span class="section-tag"><i class="fas fa-user"></i> About & Academics</span>
      <h2 class="section-title">Bridging Code, Architecture & <span class="gradient-text">Global Context</span></h2>
      <p class="section-subtitle">A synthesis of formal Computer Science foundations, hands-on production web engineering, and multilingual communication.</p>
    </div>

    <div class="about-grid">
      <div class="about-bio-card glass-card">
        <h3 class="about-card-title"><i class="fas fa-compass"></i> Engineering Philosophy</h3>
        <p class="about-p">
          I specialize in architecting scalable, maintainable, and high-throughput web applications with <strong>Python, Django, PostgreSQL, and Svelte</strong>. I focus on clean backend models, robust API contracts, and responsive, accessible user interfaces.
        </p>
        <p class="about-p">
          Being fluent in <strong>7 languages</strong> enables me to communicate effortlessly with global engineering teams, cross-functional stakeholders, and international clients across the Americas, Europe, Middle East, and South Asia.
        </p>

        <div class="about-highlights-grid">
          <div class="about-highlight-box">
            <i class="fas fa-server highlight-icon"></i>
            <div>
              <div class="highlight-title">Backend Specialist</div>
              <div class="highlight-desc">Django, DRF APIs & PostgreSQL</div>
            </div>
          </div>
          <div class="about-highlight-box">
            <i class="fas fa-bolt highlight-icon"></i>
            <div>
              <div class="highlight-title">Modern Frontend</div>
              <div class="highlight-desc">Svelte, Vite & Reactive State</div>
            </div>
          </div>
          <div class="about-highlight-box">
            <i class="fas fa-shield-alt highlight-icon"></i>
            <div>
              <div class="highlight-title">Clean Architecture</div>
              <div class="highlight-desc">Security, Caching & Modular Code</div>
            </div>
          </div>
          <div class="about-highlight-box">
            <i class="fas fa-handshake highlight-icon"></i>
            <div>
              <div class="highlight-title">Global Freelance</div>
              <div class="highlight-desc">Verified Fiverr Seller (@sajwin_sj)</div>
            </div>
          </div>
        </div>
      </div>

      <div class="about-edu-column">
        <div class="edu-card glass-card">
          <div class="edu-header">
            <div class="edu-icon"><i class="fas fa-graduation-cap"></i></div>
            <div>
              <div class="edu-tag">Undergraduate Degree</div>
              <h3 class="edu-title">{personalInfo.degree}</h3>
              <div class="edu-institution">{personalInfo.university}</div>
            </div>
          </div>
          <p class="edu-desc">
            Rigorous university curriculum covering Data Structures & Algorithms, Database Management Systems (RDBMS), Object-Oriented Software Design, Web Technologies, and Computer Networks.
          </p>
        </div>

        <div class="edu-card glass-card">
          <div class="edu-header">
            <div class="edu-icon"><i class="fas fa-laptop-code"></i></div>
            <div>
              <div class="edu-tag">Senior Secondary</div>
              <h3 class="edu-title">Computer Science & Mathematics</h3>
              <div class="edu-institution">{personalInfo.schooling}</div>
            </div>
          </div>
          <p class="edu-desc">
            Early foundational training in computational logic, algorithm design, Python programming fundamentals, and discrete mathematics.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>
