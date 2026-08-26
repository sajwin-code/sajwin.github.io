import { writable } from 'svelte/store';

export function getRouteFromUrl() {
  const base = '/sajwin.github.io';

  const path = window.location.pathname
    .replace(base, '')
    .toLowerCase()
    .replace(/\/$/, '') || '';

  if (typeof window === 'undefined') return 'home';
  
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
  
  const base = '/sajwin.github.io';
  // Check if the url already has the base, if not, prepend it
  const fullPath = url.startsWith(base) ? url : `${base}${url.startsWith('/') ? '' : '/'}${url}`;
  
  window.history.pushState({}, '', fullPath);
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