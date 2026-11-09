(() => {
  /* masthead hairline appears once the page has moved */
  const head = document.getElementById('masthead');
  if (head) {
    const onScroll = () => head.classList.toggle('is-stuck', window.scrollY > 8);
    onScroll();
    addEventListener('scroll', onScroll, {passive:true});
  }

  /* The hang. Two controls act on the same set of works: a series filter and
     a salon/grid switch. Salon varies the spans so the wall reads unevenly,
     the way a real hang does; grid resets every work to one equal cell. */
  const hang = document.getElementById('hang');
  if (!hang) return;
  const works = Array.from(hang.querySelectorAll('.work'));
  const count = document.getElementById('count');

  const filters = Array.from(document.querySelectorAll('[data-filter]'));
  const hangs   = Array.from(document.querySelectorAll('[data-sethang]'));

  const apply = (series) => {
    let shown = 0;
    works.forEach(w => {
      const hit = series === 'all' || w.dataset.series === series;
      w.hidden = !hit;
      if (hit) shown++;
    });
    if (count) count.textContent = shown + (shown === 1 ? ' work' : ' works');
  };

  filters.forEach(b => b.addEventListener('click', () => {
    filters.forEach(o => o.setAttribute('aria-pressed', String(o === b)));
    apply(b.dataset.filter);
  }));

  hangs.forEach(b => b.addEventListener('click', () => {
    hangs.forEach(o => o.setAttribute('aria-pressed', String(o === b)));
    hang.dataset.hang = b.dataset.sethang;
  }));

  apply('all');
})();
