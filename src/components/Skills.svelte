<script>
  import { skillsData } from '../data/portfolioData.js';
</script>

<section class="skills-section" id="skills">
  <div class="container">
    <div class="section-header">
      <span class="section-tag"><i class="fas fa-code"></i> Technical Stack</span>
      <h2 class="section-title">Skills & Modern <span class="gradient-text">Capabilities Matrix</span></h2>
      <p class="section-subtitle">Deep expertise across modern full-stack web technologies, relational architecture, and clean developer workflows.</p>
    </div>

    <div class="skills-categories">
      {#each skillsData as cat}
        <div class="skill-category-card glass-card">
          <div class="category-header">
            <div class="category-icon"><i class={cat.icon}></i></div>
            <h3 class="category-title">{cat.category}</h3>
          </div>
          <div class="skills-badge-grid">
            {#each cat.items as skill}
              <div class="skill-chip">
                <i class="{skill.icon} chip-icon"></i>
                <span class="chip-name">{skill.name}</span>
              </div>
            {/each}
          </div>
        </div>
      {/each}
    </div>
  </div>
</section>
