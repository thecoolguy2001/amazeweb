(() => {
  const head = document.getElementById('masthead');
  if (head) {
    const onScroll = () => head.classList.toggle('is-stuck', window.scrollY > 8);
    onScroll();
    addEventListener('scroll', onScroll, {passive:true});
  }

  /* The estimator. Everything it needs is in these three tables, so the
     published price list and the quote can never drift apart -- change a
     number here and the cards on the services page are the only other
     place to touch. */
  const est = document.getElementById('est');
  if (!est) return;

  const BASE = {            /* per visit, medium dog */
    daycare:  34,
    grooming: 48,
    training: 40,
    boarding: 46,
  };
  const SIZE = {small: 0.88, medium: 1, large: 1.18};
  const FREQ = {
    once:  {visits: 1, label: 'one visit',        discount: 0},
    two:   {visits: 8, label: '2 days a week',    discount: 0.05},
    three: {visits: 13, label: '3 days a week',   discount: 0.08},
    five:  {visits: 22, label: '5 days a week',   discount: 0.15},
  };
  const UNIT = {daycare: 'day', grooming: 'groom', training: 'session', boarding: 'night'};

  const state = {service: 'daycare', size: 'medium', freq: 'two'};
  const money = n => '£' + n.toFixed(2).replace(/\.00$/, '');

  const el = id => document.getElementById(id);
  const run = () => {
    const unit  = BASE[state.service] * SIZE[state.size];
    const f     = FREQ[state.freq];
    const gross = unit * f.visits;
    const saved = gross * f.discount;
    const total = gross - saved;

    el('est-total').textContent = money(total);
    el('est-per').textContent   = f.visits === 1
      ? 'for a single ' + UNIT[state.service]
      : 'a month, ' + f.label;
    el('est-unit').textContent  = money(unit) + ' / ' + UNIT[state.service];
    el('est-visits').textContent = f.visits === 1 ? '1' : f.visits + ' a month';
    el('est-disc').textContent  = f.discount ? '−' + money(saved) + ' (' + Math.round(f.discount*100) + '%)' : 'None';
  };

  est.querySelectorAll('[data-k]').forEach(b => b.addEventListener('click', () => {
    const k = b.dataset.k;
    est.querySelectorAll('[data-k="' + k + '"]').forEach(
      o => o.setAttribute('aria-pressed', String(o === b)));
    state[k] = b.dataset.v;
    run();
  }));
  run();
})();
