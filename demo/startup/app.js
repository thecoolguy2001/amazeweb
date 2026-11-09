(() => {
  const head = document.getElementById('masthead');
  if (head) {
    const onScroll = () => head.classList.toggle('is-stuck', window.scrollY > 8);
    onScroll();
    addEventListener('scroll', onScroll, {passive:true});
  }

  /* Pricing period. Both figures live on the element as data attributes so the
     toggle never does arithmetic and the annual saving stays whatever the
     pricing page actually says it is. */
  const toggles = Array.from(document.querySelectorAll('[data-period]'));
  if (toggles.length) {
    const figs = Array.from(document.querySelectorAll('.fig[data-m]'));
    const pers = Array.from(document.querySelectorAll('.per[data-m]'));
    const set = (p) => {
      figs.forEach(f => { f.textContent = f.dataset[p === 'year' ? 'y' : 'm']; });
      pers.forEach(f => { f.textContent = f.dataset[p === 'year' ? 'y' : 'm']; });
    };
    toggles.forEach(b => b.addEventListener('click', () => {
      toggles.forEach(o => o.setAttribute('aria-pressed', String(o === b)));
      set(b.dataset.period);
    }));
    set('month');
  }

  /* Changelog filter. */
  const log = document.getElementById('log');
  if (log) {
    const rows = Array.from(log.querySelectorAll('.entry'));
    const chips = Array.from(document.querySelectorAll('[data-kind]'));
    const shown = document.getElementById('shown');
    const apply = (kind) => {
      let n = 0;
      rows.forEach(r => {
        const hit = kind === 'all' || r.dataset.kind === kind;
        r.hidden = !hit;
        if (hit) n++;
      });
      if (shown) shown.textContent = n + (n === 1 ? ' entry' : ' entries');
    };
    chips.forEach(b => b.addEventListener('click', () => {
      chips.forEach(o => o.setAttribute('aria-pressed', String(o === b)));
      apply(b.dataset.kind);
    }));
    apply('all');
  }
})();
