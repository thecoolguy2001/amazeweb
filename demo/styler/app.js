(() => {
  const head = document.getElementById('masthead');
  if (head) {
    const onScroll = () => head.classList.toggle('is-stuck', window.scrollY > 8);
    onScroll();
    addEventListener('scroll', onScroll, {passive:true});
  }

  /* ---- lookbook hotspots -------------------------------------------------
     Each pin owns one card. Only one is open at a time, and the card is
     placed on whichever side of the pin has room so it never leaves the
     image. Opening is a click rather than a hover so it works on a phone. */
  const pins = Array.from(document.querySelectorAll('.hot'));
  const closeAll = () => pins.forEach(p => {
    p.setAttribute('aria-expanded', 'false');
    const c = document.getElementById(p.getAttribute('aria-controls'));
    if (c) c.hidden = true;
  });

  pins.forEach(pin => {
    pin.addEventListener('click', (e) => {
      e.preventDefault();
      const card = document.getElementById(pin.getAttribute('aria-controls'));
      const open = pin.getAttribute('aria-expanded') === 'true';
      closeAll();
      if (open || !card) return;

      pin.setAttribute('aria-expanded', 'true');
      card.hidden = false;

      /* Place it: below-right of the pin by default, flipped on whichever
         axis would otherwise overflow the figure. */
      const fig  = pin.closest('.look');
      const fr   = fig.getBoundingClientRect();
      const pr   = pin.getBoundingClientRect();
      const cr   = card.getBoundingClientRect();
      const left = (pr.left - fr.left) + pr.width + 12;
      const top  = (pr.top  - fr.top)  + pr.height + 12;
      card.style.left = (left + cr.width  > fr.width  ? Math.max(8, left - cr.width  - pr.width  - 24) : left) + 'px';
      card.style.top  = (top  + cr.height > fr.height ? Math.max(8, top  - cr.height - pr.height - 24) : top)  + 'px';
    });
  });
  if (pins.length) {
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.hot') && !e.target.closest('.hot-card')) closeAll();
    });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeAll(); });
  }

  /* ---- collection filter and sort --------------------------------------- */
  const grid = document.getElementById('grid');
  if (grid) {
    const items = Array.from(grid.querySelectorAll('.item'));
    const chips = Array.from(document.querySelectorAll('[data-cat]'));
    const sort  = document.getElementById('sort');
    const count = document.getElementById('count');
    let cat = 'all';

    const render = () => {
      let n = 0;
      items.forEach(i => {
        const hit = cat === 'all' || i.dataset.cat === cat;
        i.hidden = !hit;
        if (hit) n++;
      });
      if (count) count.textContent = n + (n === 1 ? ' piece' : ' pieces');
      if (sort) {
        const num = (el, k) => Number(el.dataset[k]);
        const order = {
          'new':        (a, b) => num(a,'rank')  - num(b,'rank'),
          'price-asc':  (a, b) => num(a,'price') - num(b,'price'),
          'price-desc': (a, b) => num(b,'price') - num(a,'price'),
        }[sort.value];
        if (order) items.slice().sort(order).forEach(i => grid.appendChild(i));
      }
    };
    chips.forEach(b => b.addEventListener('click', () => {
      chips.forEach(o => o.setAttribute('aria-pressed', String(o === b)));
      cat = b.dataset.cat;
      render();
    }));
    if (sort) sort.addEventListener('change', render);
    render();
  }

  /* ---- product: colour and size ----------------------------------------- */
  const pdp = document.getElementById('pdp');
  if (pdp) {
    const add   = document.getElementById('add');
    const stock = document.getElementById('stock');
    const swVal = document.getElementById('sw-val');
    const szVal = document.getElementById('sz-val');
    let colour = null, size = null;

    const sync = () => {
      if (swVal) swVal.textContent = colour || '—';
      if (szVal) szVal.textContent = size   || '—';
      const ready = Boolean(colour && size);
      if (add) {
        add.disabled = !ready;
        add.textContent = ready ? 'Add to bag' : 'Select a size';
      }
      if (stock) {
        stock.textContent = !size ? 'Free returns within 30 days. Ships in 2–3 working days.'
          : size === 'XS' ? 'Low stock — two left in this size.'
          : 'In stock. Ships in 2–3 working days.';
      }
    };
    pdp.querySelectorAll('.sw').forEach(b => b.addEventListener('click', () => {
      pdp.querySelectorAll('.sw').forEach(o => o.setAttribute('aria-pressed', String(o === b)));
      colour = b.dataset.colour; sync();
    }));
    pdp.querySelectorAll('.size').forEach(b => b.addEventListener('click', () => {
      if (b.disabled) return;
      pdp.querySelectorAll('.size').forEach(o => o.setAttribute('aria-pressed', String(o === b)));
      size = b.dataset.size; sync();
    }));
    const first = pdp.querySelector('.sw[aria-pressed="true"]');
    if (first) colour = first.dataset.colour;
    sync();
  }

  /* ---- cart --------------------------------------------------------------
     Line prices live on the row in data-price (minor units), so the markup
     stays the single source of truth and the totals can never disagree with
     what is printed next to each item. */
  const cart = document.getElementById('cart');
  if (cart) {
    const money = n => '£' + (n / 100).toFixed(2);
    const SHIP_FREE_OVER = 15000;

    const recalc = () => {
      let sub = 0, units = 0;
      cart.querySelectorAll('.line').forEach(line => {
        const price = Number(line.dataset.price);
        const q = Number(line.querySelector('.n').textContent);
        sub += price * q; units += q;
        line.querySelector('.lt').textContent = money(price * q);
      });
      const ship = units === 0 ? 0 : (sub >= SHIP_FREE_OVER ? 0 : 595);
      const set = (id, v) => { const el = document.getElementById(id); if (el) el.textContent = v; };
      set('sub', money(sub));
      set('ship', units === 0 ? '—' : (ship === 0 ? 'Free' : money(ship)));
      set('total', money(sub + ship));
      set('units', units + (units === 1 ? ' item' : ' items'));
      const note = document.getElementById('ship-note');
      if (note) note.textContent = units === 0 ? 'Your bag is empty.'
        : sub >= SHIP_FREE_OVER ? 'Shipping is free on this order.'
        : 'Spend ' + money(SHIP_FREE_OVER - sub) + ' more for free shipping.';
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
        const next = Math.max(1, Math.min(9, Number(n.textContent) + Number(btn.dataset.step)));
        n.textContent = next;
        recalc();
      }
      if (btn.dataset.remove !== undefined) { line.remove(); recalc(); }
    });
    recalc();
  }
})();
