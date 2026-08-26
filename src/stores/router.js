import { writable } from 'svelte/store';

export function getRouteFromUrl() {
  if (typeof window === 'undefined') return 'home';
  
  const path = window.location.pathname.toLowerCase().replace(/\/$/, '') || '';
  const hash = window.location.hash.toLowerCase().replace(/^#\/?/, '').replace(/\/$/, '');

  if (path === '/linktree/polix' || hash === 'linktree/polix' || hash === '/linktree/polix') {
    return 'polix';
  }
  if (path === '/linktree' || hash === 'linktree' || hash === '/linktree') {
    return 'linktree';
  }
  return 'home';
}

export const currentRoute = writable(getRouteFromUrl());

export function navigate(url) {
  if (typeof window === 'undefined') return;
  window.history.pushState({}, '', url);
  currentRoute.set(getRouteFromUrl());
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

if (typeof window !== 'undefined') {
  window.addEventListener('popstate', () => {
    currentRoute.set(getRouteFromUrl());
  });
  window.addEventListener('hashchange', () => {
    currentRoute.set(getRouteFromUrl());
  });
}