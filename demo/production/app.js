(() => {
  const head = document.getElementById('masthead');
  if (head) {
    const onScroll = () => head.classList.toggle('is-stuck', window.scrollY > 8);
    onScroll();
    addEventListener('scroll', onScroll, {passive:true});
  }

  /* Scrubbing. Moving a pointer across a tile steps through its frames and
     moves the timecode with it, so the grid behaves like film rather than
     like stills. Frame 0 is what everyone else sees: touch devices, reduced
     motion, and anyone whose pointer never enters the tile. */
  const fine = matchMedia('(hover:hover) and (pointer:fine)').matches;
  const calm = matchMedia('(prefers-reduced-motion:reduce)').matches;

  document.querySelectorAll('.tile').forEach(tile => {
    const frames = Array.from(tile.querySelectorAll('.frame'));
    if (!frames.length) return;

    const scrub = tile.querySelector('.scrub');
    const badge = tile.querySelector('.tc-badge');
    const secs  = Number(tile.dataset.dur || 90);
    let ticks = [];

    if (scrub) {
      scrub.innerHTML = '';
      ticks = frames.map(() => scrub.appendChild(document.createElement('i')));
    }

    const show = (i) => {
      frames.forEach((f, n) => f.classList.toggle('on', n === i));
      ticks.forEach((t, n) => t.classList.toggle('on', n === i));
      if (badge) {
        const at = Math.round(secs * (i / Math.max(1, frames.length - 1)));
        const mm = String(Math.floor(at / 60)).padStart(2, '0');
        const ss = String(at % 60).padStart(2, '0');
        badge.textContent = mm + ':' + ss;
      }
    };
    show(0);
    if (!fine || calm) return;

    tile.addEventListener('pointermove', e => {
      const b = tile.getBoundingClientRect();
      const p = Math.min(0.9999, Math.max(0, (e.clientX - b.left) / b.width));
      show(Math.floor(p * frames.length));
    });
    tile.addEventListener('pointerleave', () => show(0));
  });

  /* Work filter. */
  const reel = document.getElementById('reel');
  if (reel) {
    const tiles = Array.from(reel.querySelectorAll('.tile'));
    const chips = Array.from(document.querySelectorAll('[data-cat]'));
    const count = document.getElementById('count');
    const apply = (cat) => {
      let n = 0;
      tiles.forEach(t => {
        const hit = cat === 'all' || t.dataset.cat === cat;
        t.hidden = !hit;
        if (hit) n++;
      });
      if (count) count.textContent = n + (n === 1 ? ' project' : ' projects');
    };
    chips.forEach(b => b.addEventListener('click', () => {
      chips.forEach(o => o.setAttribute('aria-pressed', String(o === b)));
      apply(b.dataset.cat);
    }));
    apply('all');
  }
})();
