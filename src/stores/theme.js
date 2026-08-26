import { writable } from 'svelte/store';

const getInitialTheme = () => {
  if (typeof localStorage !== 'undefined') {
    return localStorage.getItem('sajwin-theme') || 
      (typeof window !== 'undefined' && window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
  }
  return 'dark';
};

const initial = getInitialTheme();
export const theme = writable(initial);

if (typeof document !== 'undefined') {
  document.documentElement.setAttribute('data-theme', initial);
}

export function toggleTheme() {
  theme.update(current => {
    const next = current === 'light' ? 'dark' : 'light';
    if (typeof document !== 'undefined') {
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('sajwin-theme', next);
    }
    return next;
  });
}
