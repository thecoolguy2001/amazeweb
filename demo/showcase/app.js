(() => {
  const head = document.getElementById('masthead');
  const onScroll = () => head.classList.toggle('is-stuck', window.scrollY > 8);
  onScroll();
  addEventListener('scroll', onScroll, {passive:true});

  const peek = document.getElementById('peek');
  const fine = matchMedia('(hover:hover) and (pointer:fine)').matches;
  const calm = matchMedia('(prefers-reduced-motion:reduce)').matches;
  if (!peek || !fine || calm) return;

  let x = 0, y = 0, cx = 0, cy = 0, live = false, frame = null;

  const loop = () => {
    cx += (x - cx) * 0.16;
    cy += (y - cy) * 0.16;
    peek.style.transform = `translate3d(${cx}px, ${cy}px, 0)`;
    frame = live ? requestAnimationFrame(loop) : null;
  };

  document.querySelectorAll('.entry').forEach(row => {
    row.addEventListener('pointerenter', e => {
      peek.className = 'peek plate ' + row.dataset.plate;
      x = cx = e.clientX + 28;
      y = cy = e.clientY - 40;
      peek.style.transform = `translate3d(${cx}px, ${cy}px, 0)`;
      peek.classList.add('on');
      if (!frame) { live = true; frame = requestAnimationFrame(loop); }
    });
    row.addEventListener('pointermove', e => {
      const r = peek.getBoundingClientRect();
      x = Math.min(e.clientX + 28, innerWidth - r.width - 16);
      y = Math.min(Math.max(e.clientY - 40, 16), innerHeight - r.height - 16);
    });
    row.addEventListener('pointerleave', () => {
      peek.classList.remove('on');
      live = false;
    });
  });
})();
