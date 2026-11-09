(() => {
  const head = document.getElementById('masthead');
  if (head) {
    const onScroll = () => head.classList.toggle('is-stuck', window.scrollY > 8);
    onScroll();
    addEventListener('scroll', onScroll, {passive:true});
  }

  /* ---- the routine builder ----------------------------------------------
     One catalogue, one table of routines. A routine is three product keys
     plus the sentence explaining why those three and in that order, which
     is the part that actually sells skincare. Prices are in pence and come
     from the same catalogue the shop grid is built from, so a price change
     lands in both places at once. */
  const CATALOGUE = {
    milk:    {name: 'Quiet Milk Cleanser',   plate: 'b2', price: 2400, size: '150ml', step: 'Cleanse'},
    gel:     {name: 'Clear Gel Cleanser',    plate: 'b4', price: 2200, size: '150ml', step: 'Cleanse'},
    mist:    {name: 'Barrier Mist',          plate: 'b3', price: 1900, size: '100ml', step: 'Prep'},
    serumB:  {name: 'Bright Serum 10%',      plate: 'b5', price: 3800, size: '30ml',  step: 'Treat'},
    serumN:  {name: 'Calm Serum',            plate: 'b6', price: 3400, size: '30ml',  step: 'Treat'},
    serumR:  {name: 'Renew Serum 0.3%',      plate: 'b1', price: 4200, size: '30ml',  step: 'Treat'},
    cream:   {name: 'Rich Night Cream',      plate: 'b1', price: 3600, size: '50ml',  step: 'Seal'},
    light:   {name: 'Light Day Cream',       plate: 'b2', price: 3200, size: '50ml',  step: 'Seal'},
    spf:     {name: 'Daily SPF 50',          plate: 'b4', price: 2800, size: '50ml',  step: 'Protect'},
    balm:    {name: 'Repair Balm',           plate: 'b5', price: 2600, size: '30ml',  step: 'Seal'},
  };

  const ROUTINES = {
    'dry-am':       {keys: ['milk','mist','spf'],        why: 'Dry skin loses water faster than it loses oil, so the morning job is to put water on and then stop it leaving. Mist while damp, seal, and let the SPF do the last layer.'},
    'dry-pm':       {keys: ['milk','serumN','cream'],     why: 'A gentle cleanse so you are not stripping what little oil there is, something calming while the barrier rebuilds overnight, then the richest thing you own on top.'},
    'breakouts-am': {keys: ['gel','serumN','spf'],        why: 'Resist the urge to use anything harsh in the morning. Clean, calm, protect — most breakout routines fail because they do too much twice a day.'},
    'breakouts-pm': {keys: ['gel','serumR','light'],      why: 'The active goes at night, at a low strength, three times a week to begin with. A light cream still goes over it; skipping moisturiser is what makes actives hurt.'},
    'dull-am':      {keys: ['milk','serumB','spf'],       why: 'Vitamin C in the morning and SPF straight over it. The two work better together than either does alone, and without the SPF the serum is largely wasted.'},
    'dull-pm':      {keys: ['milk','serumR','cream'],     why: 'Gentle exfoliation at night does the work that brightening serums get the credit for. Start at twice a week and build up slowly.'},
    'sensitive-am': {keys: ['milk','mist','spf'],         why: 'Three steps, no actives, nothing with fragrance. If your skin is reacting, the answer is almost always fewer products rather than a better one.'},
    'sensitive-pm': {keys: ['milk','serumN','balm'],      why: 'Cleanse, calm, and seal with a balm rather than a lotion — fewer emulsifiers, which is usually what sensitive skin is objecting to.'},
  };

  const builder = document.getElementById('builder');
  if (builder) {
    const state = {concern: 'dry', time: 'am'};
    const money = n => '£' + (n / 100).toFixed(2).replace(/\.00$/, '');
    const out = document.getElementById('routine-steps');
    const ttl = document.getElementById('routine-title');
    const tot = document.getElementById('routine-total');
    const why = document.getElementById('routine-why');

    const render = () => {
      const r = ROUTINES[state.concern + '-' + state.time];
      if (!r || !out) return;
      let sum = 0;
      out.innerHTML = r.keys.map((k, i) => {
        const p = CATALOGUE[k];
        sum += p.price;
        return '<div class="step">' +
          '<span class="plate ' + p.plate + '" aria-hidden="true"></span>' +
          '<div><p class="n">Step ' + (i + 1) + ' — ' + p.step + '</p>' +
          '<h4>' + p.name + '</h4><p>' + p.size + '</p></div>' +
          '<span class="pr">' + money(p.price) + '</span></div>';
      }).join('');
      const label = builder.querySelector('[data-concern="' + state.concern + '"]').textContent.trim();
      const when  = state.time === 'am' ? 'Morning' : 'Evening';
      if (ttl) ttl.textContent = when + ' — ' + label.toLowerCase();
      if (tot) tot.textContent = money(sum) + ' for three steps';
      if (why) why.textContent = r.why;
    };

    builder.querySelectorAll('[data-concern]').forEach(b => b.addEventListener('click', () => {
      builder.querySelectorAll('[data-concern]').forEach(o => o.setAttribute('aria-pressed', String(o === b)));
      state.concern = b.dataset.concern; render();
    }));
    builder.querySelectorAll('[data-time]').forEach(b => b.addEventListener('click', () => {
      builder.querySelectorAll('[data-time]').forEach(o => o.setAttribute('aria-pressed', String(o === b)));
      state.time = b.dataset.time; render();
    }));
    render();
  }

  /* ---- shop filter ------------------------------------------------------- */
  const grid = document.getElementById('grid');
  if (grid) {
    const cards = Array.from(grid.querySelectorAll('.card'));
    const chips = Array.from(document.querySelectorAll('[data-step-filter]'));
    const count = document.getElementById('count');
    chips.forEach(b => b.addEventListener('click', () => {
      chips.forEach(o => o.setAttribute('aria-pressed', String(o === b)));
      const k = b.dataset.stepFilter;
      let n = 0;
      cards.forEach(c => {
        const hit = k === 'all' || c.dataset.step === k;
        c.hidden = !hit;
        if (hit) n++;
      });
      if (count) count.textContent = n + (n === 1 ? ' product' : ' products');
    }));
  }

  /* ---- product size picker ----------------------------------------------- */
  const pdp = document.getElementById('pdp');
  if (pdp) {
    const price = document.getElementById('pdp-price');
    pdp.querySelectorAll('.sizebtn').forEach(b => b.addEventListener('click', () => {
      pdp.querySelectorAll('.sizebtn').forEach(o => o.setAttribute('aria-pressed', String(o === b)));
      if (price) price.textContent = b.dataset.price;
    }));
  }

  /* ---- cart --------------------------------------------------------------- */
  const cart = document.getElementById('cart');
  if (cart) {
    const FREE_OVER = 5000;
    const money = n => '£' + (n / 100).toFixed(2);
    const set = (id, v) => { const el = document.getElementById(id); if (el) el.textContent = v; };
    const recalc = () => {
      let sub = 0, units = 0;
      cart.querySelectorAll('.line').forEach(line => {
        const p = Number(line.dataset.price);
        const q = Number(line.querySelector('.n').textContent);
        sub += p * q; units += q;
        line.querySelector('.lt').textContent = money(p * q);
      });
      const ship = units === 0 ? 0 : (sub >= FREE_OVER ? 0 : 395);
      set('sub', money(sub));
      set('ship', units === 0 ? '—' : (ship === 0 ? 'Free' : money(ship)));
      set('total', money(sub + ship));
      set('units', units + (units === 1 ? ' item' : ' items'));
      set('bagcount', String(units));
      const note = document.getElementById('ship-note');
      if (note) note.textContent = units === 0 ? 'Your bag is empty.'
        : sub >= FREE_OVER ? 'Free delivery and two samples of your choice are included.'
        : money(FREE_OVER - sub) + ' more for free delivery.';
      const empty = document.getElementById('empty');
      if (empty) empty.hidden = units !== 0;
    };
    cart.addEventListener('click', (e) => {
      const btn = e.target.closest('button');
      if (!btn) return;
      const line = btn.closest('.line');
      if (!line) return;
      if (btn.dataset.step) {
        const n = line.querySelector('.n');
        n.textContent = Math.max(1, Math.min(9, Number(n.textContent) + Number(btn.dataset.step)));
        recalc();
      }
      if (btn.dataset.remove !== undefined) { line.remove(); recalc(); }
    });
    recalc();
  }
})();
