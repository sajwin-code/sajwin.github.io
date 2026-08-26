<script>
  import { currentRoute } from './stores/router.js';
  import Navbar from './components/Navbar.svelte';
  import Hero from './components/Hero.svelte';
  import Stats from './components/Stats.svelte';
  import About from './components/About.svelte';
  import Globe from './components/Globe.svelte';
  import Skills from './components/Skills.svelte';
  import Projects from './components/Projects.svelte';
  import Pricing from './components/Pricing.svelte';
  import Services from './components/Services.svelte';
  import Contact from './components/Contact.svelte';
  import Footer from './components/Footer.svelte';
  import Toast from './components/Toast.svelte';
  import BackToTop from './components/BackToTop.svelte';
  
  import Linktree from './pages/Linktree.svelte';
  import PolixLinktree from './pages/PolixLinktree.svelte';
</script>

<div class="app-root">
  {#if $currentRoute === 'linktree'}
    <Linktree />
  {:else if $currentRoute === 'polix'}
    <PolixLinktree />
  {:else}
    <Navbar />
    <main>
      <Hero />
      <Stats />
      <About />
      <Globe />
      <Skills />
      <Projects />
      <Pricing />
      <Services />
      <Contact />
    </main>
    <Footer />
    <BackToTop />
  {/if}
  <Toast />
</div>

<style>
  .app-root {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }
  main {
    flex: 1;
  }
</style>
