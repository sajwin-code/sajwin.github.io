import { writable } from 'svelte/store';

export const currency = writable('INR');

export function toggleCurrency() {
  currency.update(curr => curr === 'INR' ? 'USD' : 'INR');
}

export function setCurrency(curr) {
  currency.set(curr);
}
