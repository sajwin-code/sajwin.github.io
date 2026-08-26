import { writable } from 'svelte/store';

export const toast = writable({ message: '', visible: false });

let timeoutId = null;

export function showToast(message, duration = 3500) {
  if (timeoutId) clearTimeout(timeoutId);
  toast.set({ message, visible: true });
  timeoutId = setTimeout(() => {
    toast.set({ message: '', visible: false });
  }, duration);
}

export function copyToClipboard(text, label = 'Text') {
  if (typeof navigator !== 'undefined' && navigator.clipboard) {
    navigator.clipboard.writeText(text).then(() => {
      showToast(`Copied ${label} to clipboard!`);
    }).catch(() => {
      fallbackCopy(text, label);
    });
  } else {
    fallbackCopy(text, label);
  }
}

function fallbackCopy(text, label) {
  if (typeof document === 'undefined') return;
  const textArea = document.createElement('textarea');
  textArea.value = text;
  document.body.appendChild(textArea);
  textArea.select();
  document.execCommand('copy');
  document.body.removeChild(textArea);
  showToast(`Copied ${label} to clipboard!`);
}

