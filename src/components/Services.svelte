<script>
  import { servicesData } from '../data/portfolioData.js';
</script>

<section class="services-section" id="services">
  <div class="container">
    <div class="section-header">
      <span class="section-tag"><i class="fas fa-cogs"></i> Offerings</span>
      <h2 class="section-title">Development & Architectural <span class="gradient-text">Services</span></h2>
      <p class="section-subtitle">Comprehensive software development capabilities from concept and database modeling to deployment and scaling.</p>
    </div>

    <div class="services-grid">
      {#each servicesData as srv}
        <div class="service-card glass-card">
          <div class="service-icon"><i class={srv.icon}></i></div>
          <h3 class="service-title">{srv.title}</h3>
          <p class="service-desc">{srv.description}</p>
          <ul class="service-deliverables">
            {#each srv.deliverables as del}
              <li><i class="fas fa-check-circle check-icon"></i> {del}</li>
            {/each}
          </ul>
        </div>
      {/each}
    </div>
  </div>
</section>
