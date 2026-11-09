(() => {
  const head = document.getElementById('masthead');
  if (head) {
    const onScroll = () => head.classList.toggle('is-stuck', window.scrollY > 8);
    onScroll();
    addEventListener('scroll', onScroll, {passive:true});
  }

  /* ---- deliver / reserve -------------------------------------------------
     A boutique's advantage is the building, so the whole storefront can be
     read either way round. Each product carries two stock numbers --
     data-online and data-shop -- and the switch rewrites every availability
     line, every call to action and the delivery copy from whichever one is
     in play. The two numbers genuinely differ, which is the point: the
     brass lamp is sold out online and sitting in the window. */
  const MODE_COPY = {
    deliver: {
      note: 'Sent from the shop by hand, usually the next working day. <b>Free over £75</b>, and we will text you a photo of it packed if you ask.',
      cta: 'Add to basket',
      many: n => n > 3 ? 'In stock online' : 'Only ' + n + ' left online',
      none: 'Sold out online',
    },
    reserve: {
      note: 'We will hold it on the counter for <b>48 hours</b> under your name, with nothing to pay now. Try it, turn it over, and decide in the shop.',
      cta: 'Reserve to try on',
      many: n => n > 1 ? 'On the shelf today' : 'One in the shop — last one',
      none: 'Not in the shop today',
    },
  };

  let mode = 'deliver';

  const paint = () => {
    const copy = MODE_COPY[mode];

    document.querySelectorAll('[data-online]').forEach(el => {
      const n = Number(mode === 'deliver' ? el.dataset.online : el.dataset.shop);
      const line = el.querySelector('.avail');
      if (line) {
        line.textContent = n > 0 ? copy.many(n) : copy.none;
        line.classList.toggle('none', n === 0);
      }
      const cta = el.querySelector('[data-cta]');
      if (cta) {
        const out = n === 0;
        cta.textContent = out
          ? (mode === 'deliver' ? 'Email me when it is back' : 'Ask us to get it in')
          : copy.cta;
        cta.classList.toggle('gold', mode === 'reserve' && !out);
      }
    });

    document.querySelectorAll('[data-mode-note]').forEach(el => { el.innerHTML = copy.note; });
    document.querySelectorAll('[data-mode]').forEach(b =>
      b.setAttribute('aria-pressed', String(b.dataset.mode === mode)));
  };

  document.querySelectorAll('[data-mode]').forEach(b => b.addEventListener('click', () => {
    mode = b.dataset.mode;
    paint();
  }));
  paint();

  /* ---- collection filter -------------------------------------------------- */
  const grid = document.getElementById('grid');
  if (grid) {
    const cards = Array.from(grid.querySelectorAll('.card'));
    const chips = Array.from(document.querySelectorAll('[data-cat]'));
    const count = document.getElementById('count');
    chips.forEach(b => b.addEventListener('click', () => {
      chips.forEach(o => o.setAttribute('aria-pressed', String(o === b)));
      const k = b.dataset.cat;
      let n = 0;
      cards.forEach(c => {
        const hit = k === 'all' || c.dataset.cat === k;
        c.hidden = !hit;
        if (hit) n++;
      });
      if (count) count.textContent = n + (n === 1 ? ' piece' : ' pieces');
    }));
  }

  /* ---- cart ---------------------------------------------------------------
     Reserved lines are not charged now, so they are counted and shown but
     left out of the amount due -- otherwise the total would be a lie. */
  const cart = document.getElementById('cart');
  if (cart) {
    const FREE_OVER = 7500;
    const money = n => '£' + (n / 100).toFixed(2);
    const set = (id, v) => { const el = document.getElementById(id); if (el) el.textContent = v; };

    const recalc = () => {
      let pay = 0, held = 0, units = 0;
      cart.querySelectorAll('.line').forEach(line => {
        const p = Number(line.dataset.price);
        const q = Number(line.querySelector('.n').textContent);
        const reserved = line.dataset.fulfil === 'reserve';
        const lineTotal = p * q;
        units += q;
        if (reserved) held += lineTotal; else pay += lineTotal;
        line.querySelector('.lt').textContent = money(lineTotal);
      });
      const ship = pay === 0 ? 0 : (pay >= FREE_OVER ? 0 : 450);
      set('sub', money(pay));
      set('ship', pay === 0 ? '—' : (ship === 0 ? 'Free' : money(ship)));
      set('held', held === 0 ? '—' : money(held) + ' on collection');
      set('total', money(pay + ship));
      set('units', units + (units === 1 ? ' item' : ' items'));
      set('bagcount', String(units));
      const note = document.getElementById('ship-note');
      if (note) note.textContent = units === 0 ? 'Your basket is empty.'
        : held > 0 && pay === 0 ? 'Nothing to pay now — everything here is reserved for the shop.'
        : pay >= FREE_OVER ? 'Delivery is free on this order.'
        : money(FREE_OVER - pay) + ' more for free delivery.';
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
      if (btn.dataset.swap !== undefined) {
        const to = line.dataset.fulfil === 'reserve' ? 'deliver' : 'reserve';
        line.dataset.fulfil = to;
        line.querySelector('.how').textContent = to === 'reserve' ? 'Reserved to try in the shop' : 'Delivered';
        btn.textContent = to === 'reserve' ? 'Have it delivered instead' : 'Reserve it in the shop instead';
        recalc();
      }
    });
    recalc();
  }
})();
