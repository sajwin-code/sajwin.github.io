<script>
  import { onMount } from 'svelte';
  import { statsData } from '../data/portfolioData.js';

  let currentCounts = statsData.map(() => 0);
  let hasAnimated = false;
  let sectionElement;

  function animate() {
    if (hasAnimated || !sectionElement) return;
    const rect = sectionElement.getBoundingClientRect();
    if (rect.top <= window.innerHeight * 0.88) {
      hasAnimated = true;
      statsData.forEach((stat, i) => {
        let current = 0;
        const target = stat.target;
        const increment = Math.ceil(target / 35);
        const timer = setInterval(() => {
          current += increment;
          if (current >= target) {
            currentCounts[i] = target;
            clearInterval(timer);
          } else {
            currentCounts[i] = current;
          }
        }, 35);
      });
    }
  }

  onMount(() => {
    window.addEventListener('scroll', animate, { passive: true });
    animate();
    return () => window.removeEventListener('scroll', animate);
  });
</script>

<section class="stats-section" bind:this={sectionElement}>
  <div class="container">
    <div class="stats-grid">
      {#each statsData as stat, index}
        <div class="stat-card glass-card">
          <div class="stat-number">{currentCounts[index]}{stat.suffix}</div>
          <div class="stat-label">{stat.label}</div>
        </div>
      {/each}
    </div>
  </div>
</section>
