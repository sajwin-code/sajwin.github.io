<script>
  import { projectsData } from '../data/portfolioData.js';
</script>

<section class="projects-section" id="projects">
  <div class="container">
    <div class="section-header">
      <span class="section-tag"><i class="fas fa-layer-group"></i> GitHub Repositories</span>
      <h2 class="section-title">Featured Web <span class="gradient-text">Projects</span></h2>
      <p class="section-subtitle">Real-world applications built with Python, Django, PostgreSQL, and modern reactive frontends, available directly on GitHub.</p>
    </div>

    <div class="projects-grid two-column">
      {#each projectsData as proj (proj.id)}
        <div class="project-card glass-card">
          <div class="project-header">
            <div class="project-icon-box"><i class={proj.icon}></i></div>
            <span class="project-badge" class:badge-wip={proj.statusClass === 'status-wip'}>{proj.badge}</span>
          </div>

          <h3 class="project-title">{proj.title}</h3>
          <p class="project-description">{proj.description}</p>

          {#if proj.highlights}
            <ul class="project-highlights-list">
              {#each proj.highlights as item}
                <li><i class="fas fa-check-circle highlight-bullet"></i> {item}</li>
              {/each}
            </ul>
          {/if}

          <div class="project-tags">
            {#each proj.tags as tag}
              <span class="tech-tag">{tag}</span>
            {/each}
          </div>

          <div class="project-links">
            <a href={proj.github} target="_blank" rel="noopener noreferrer" class="btn-proj btn-proj-primary">
              <i class="fab fa-github"></i> View Repository
            </a>
          </div>
        </div>
      {/each}
    </div>

    <div class="github-profile-banner glass-card">
      <div class="gh-banner-content">
        <i class="fab fa-github gh-banner-icon"></i>
        <div>
          <h4 class="gh-banner-title">Explore More Code on GitHub</h4>
          <p class="gh-banner-subtitle">Browse recent commits, experimental modules, and open-source contributions @sajwin-code.</p>
        </div>
      </div>
      <a href="https://github.com/sajwin-code" target="_blank" rel="noopener noreferrer" class="btn btn-outline">
        <i class="fas fa-external-link-alt"></i> github.com/sajwin-code
      </a>
    </div>
  </div>
</section>

<style>
  .projects-grid.two-column {
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem;
    margin-bottom: 2.5rem;
  }
  @media (max-width: 900px) {
    .projects-grid.two-column {
      grid-template-columns: 1fr;
    }
  }
  .project-highlights-list {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    margin-block: 0.25rem;
    list-style: none;
    padding: 0;
  }
  .project-highlights-list li {
    font-size: 0.85rem;
    color: var(--text-secondary);
    display: flex;
    align-items: flex-start;
    gap: 0.5rem;
    line-height: 1.5;
  }
  .highlight-bullet {
    color: var(--primary);
    font-size: 0.85rem;
    margin-top: 3px;
    flex-shrink: 0;
  }
  .badge-wip {
    background: rgba(245, 158, 11, 0.12);
    color: #fbbf24;
    border-color: rgba(245, 158, 11, 0.25);
  }
  .github-profile-banner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.5rem 2rem;
    gap: 1.5rem;
    flex-wrap: wrap;
  }
  .gh-banner-content {
    display: flex;
    align-items: center;
    gap: 1.25rem;
  }
  .gh-banner-icon {
    font-size: 2.2rem;
    color: var(--text-primary);
  }
  .gh-banner-title {
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--text-primary);
  }
  .gh-banner-subtitle {
    font-size: 0.88rem;
    color: var(--text-secondary);
    margin-top: 0.2rem;
  }
</style>
