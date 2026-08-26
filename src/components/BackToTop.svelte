<script>
  import { onMount } from 'svelte';

  let visible = false;

  function handleScroll() {
    visible = window.pageYOffset > 400;
  }

  function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  onMount(() => {
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  });
</script>

<button 
  class="back-to-top" 
  class:visible={visible} 
  on:click={scrollToTop} 
  aria-label="Back to Top" 
  title="Back to Top"
>
  <i class="fas fa-chevron-up"></i>
</button>
