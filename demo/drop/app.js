/* Drop — countdown. Set data-launch on the clock, or edit TARGET below.
   If the date has passed, it rolls forward a year so the demo never shows zeros. */
(() => {
  const clock = document.getElementById('clock');
  if (!clock) return;

  const TARGET = clock.dataset.launch || '2026-03-05T10:00:00+01:00';
  let end = new Date(TARGET);
  while (end.getTime() < Date.now()) end.setFullYear(end.getFullYear() + 1);

  const slot = {
    d: clock.querySelector('[data-d]'),
    h: clock.querySelector('[data-h]'),
    m: clock.querySelector('[data-m]'),
    s: clock.querySelector('[data-s]')
  };
  const pad = n => String(n).padStart(2, '0');

  const tick = () => {
    let left = Math.max(0, end.getTime() - Date.now());
    const d = Math.floor(left / 864e5); left -= d * 864e5;
    const h = Math.floor(left / 36e5);  left -= h * 36e5;
    const m = Math.floor(left / 6e4);   left -= m * 6e4;
    const s = Math.floor(left / 1e3);
    slot.d.textContent = pad(d);
    slot.h.textContent = pad(h);
    slot.m.textContent = pad(m);
    slot.s.textContent = pad(s);
  };

  tick();
  setInterval(tick, 1000);
})();
