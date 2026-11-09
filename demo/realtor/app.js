(() => {
  const head = document.getElementById('masthead');
  if (head) {
    const onScroll = () => head.classList.toggle('is-stuck', window.scrollY > 8);
    onScroll();
    addEventListener('scroll', onScroll, {passive:true});
  }

  /* Listings: filter by type and sort, both reading values straight off the
     card's data attributes so the markup stays the single source of truth. */
  const grid = document.getElementById('grid');
  if (grid) {
    const cards = Array.from(grid.querySelectorAll('.lst'));
    const chips = Array.from(document.querySelectorAll('[data-type]'));
    const sort  = document.getElementById('sort');
    const count = document.getElementById('count');
    let type = 'all';

    const render = () => {
      let shown = 0;
      cards.forEach(c => {
        const hit = type === 'all' || c.dataset.type === type;
        c.hidden = !hit;
        if (hit) shown++;
      });
      if (count) count.textContent = shown + (shown === 1 ? ' property' : ' properties');

      if (sort) {
        const n = (el, k) => Number(el.dataset[k]);
        const order = {
          'price-desc': (a, b) => n(b,'price') - n(a,'price'),
          'price-asc':  (a, b) => n(a,'price') - n(b,'price'),
          'newest':     (a, b) => n(a,'days')  - n(b,'days'),
          'ppsf':       (a, b) => n(a,'ppsf')  - n(b,'ppsf'),
        }[sort.value];
        if (order) cards.slice().sort(order).forEach(c => grid.appendChild(c));
      }
    };

    chips.forEach(b => b.addEventListener('click', () => {
      chips.forEach(o => o.setAttribute('aria-pressed', String(o === b)));
      type = b.dataset.type;
      render();
    }));
    if (sort) sort.addEventListener('change', render);
    render();
  }

  /* Monthly estimate. Standard amortisation, rounded to the dollar. It is an
     illustration with the assumptions printed underneath, not a quote. */
  const calc = document.getElementById('calc');
  if (calc) {
    const price = Number(calc.dataset.price);
    const tax   = Number(calc.dataset.tax   || 0);   /* annual */
    const hoa   = Number(calc.dataset.hoa   || 0);   /* monthly */
    const down  = document.getElementById('down');
    const rate  = document.getElementById('rate');
    const term  = document.getElementById('term');
    const out   = document.getElementById('monthly');
    const dv    = document.getElementById('downv');
    const rv    = document.getElementById('ratev');
    const money = n => '$' + Math.round(n).toLocaleString('en-US');

    const run = () => {
      const pct = Number(down.value);
      const r   = Number(rate.value) / 100 / 12;
      const n   = Number(term.value) * 12;
      const principal = price * (1 - pct / 100);
      const pi = r === 0 ? principal / n
               : principal * r / (1 - Math.pow(1 + r, -n));
      out.textContent = money(pi + tax / 12 + hoa);
      dv.textContent = pct + '% · ' + money(price * pct / 100);
      rv.textContent = Number(rate.value).toFixed(2) + '%';
    };
    [down, rate, term].forEach(el => el && el.addEventListener('input', run));
    run();
  }
})();
