(() => {
  const head = document.getElementById('masthead');
  if (head) {
    const onScroll = () => head.classList.toggle('is-stuck', window.scrollY > 8);
    onScroll();
    addEventListener('scroll', onScroll, {passive:true});
  }

  const COLOURS = ['c-espresso','c-tan','c-sage','c-bone','c-black'];

  /* ---- swatches ----------------------------------------------------------
     Shared by the grid cards and the product page. The swatch owns the
     colour class; clicking swaps it on the plates inside the same block and
     updates the printed colour name, so the artwork and the label can never
     disagree. Which sizes are gone is per colour, carried in data-gone. */
  const paintBlock = (block, btn) => {
    const cls  = btn.dataset.swatch;
    const name = btn.dataset.name;
    block.querySelectorAll('.sw').forEach(o => o.setAttribute('aria-pressed', String(o === btn)));
    block.querySelectorAll('.plate').forEach(p => {
      COLOURS.forEach(c => p.classList.remove(c));
      p.classList.add(cls);
    });
    const label = block.querySelector('.cname, .c-val');
    if (label) label.textContent = name;

    const gone = (btn.dataset.gone || '').split(',').filter(Boolean);
    block.querySelectorAll('.sizes-avail span').forEach(s => {
      s.classList.toggle('gone', gone.includes(s.textContent.trim()));
    });
    block.querySelectorAll('.size').forEach(s => {
      const out = gone.includes(s.dataset.size);
      s.disabled = out;
      if (out) s.setAttribute('aria-pressed', 'false');
    });
    return gone;
  };

  document.querySelectorAll('.card').forEach(card => {
    card.querySelectorAll('.sw').forEach(btn => {
      btn.addEventListener('click', (e) => { e.preventDefault(); paintBlock(card, btn); });
    });
    /* Apply the starting colour's sold-out sizes on load, so the card does
       not claim every size is available until someone touches a swatch. */
    const start = card.querySelector('.sw[aria-pressed="true"]');
    if (start) paintBlock(card, start);
  });

  /* ---- shop filter and sort --------------------------------------------- */
  const grid = document.getElementById('grid');
  if (grid) {
    const cards = Array.from(grid.querySelectorAll('.card'));
    const chips = Array.from(document.querySelectorAll('[data-cat]'));
    const sort  = document.getElementById('sort');
    const count = document.getElementById('count');
    let cat = 'all';
    const render = () => {
      let n = 0;
      cards.forEach(c => {
        const hit = cat === 'all' || c.dataset.cat === cat;
        c.hidden = !hit;
        if (hit) n++;
      });
      if (count) count.textContent = n + (n === 1 ? ' style' : ' styles');
      if (sort) {
        const v = (el, k) => Number(el.dataset[k]);
        const order = {
          'new':        (a,b) => v(a,'rank')  - v(b,'rank'),
          'price-asc':  (a,b) => v(a,'price') - v(b,'price'),
          'price-desc': (a,b) => v(b,'price') - v(a,'price'),
        }[sort.value];
        if (order) cards.slice().sort(order).forEach(c => grid.appendChild(c));
      }
    };
    chips.forEach(b => b.addEventListener('click', () => {
      chips.forEach(o => o.setAttribute('aria-pressed', String(o === b)));
      cat = b.dataset.cat; render();
    }));
    if (sort) sort.addEventListener('change', render);
    render();
  }

  /* ---- product ----------------------------------------------------------- */
  const pdp = document.getElementById('pdp');
  if (pdp) {
    const add = document.getElementById('add');
    const stock = document.getElementById('stock');
    const szVal = document.getElementById('sz-val');
    let size = null;

    const sync = () => {
      if (szVal) szVal.textContent = size || 'Choose';
      if (add) { add.disabled = !size; add.textContent = size ? 'Add to bag' : 'Choose a size'; }
      if (stock) stock.textContent = !size
        ? 'Free UK delivery over £120. Ninety days to return it.'
        : (size === 'XS' || size === 'XL' ? 'Only a couple left in this size.' : 'In stock, ships tomorrow.');
    };
    pdp.querySelectorAll('.sw').forEach(btn => btn.addEventListener('click', (e) => {
      e.preventDefault();
      const gone = paintBlock(pdp, btn);
      if (size && gone.includes(size)) { size = null; }   /* colour sold out in that size */
      sync();
    }));
    pdp.querySelectorAll('.size').forEach(b => b.addEventListener('click', () => {
      if (b.disabled) return;
      pdp.querySelectorAll('.size').forEach(o => o.setAttribute('aria-pressed', String(o === b)));
      size = b.dataset.size; sync();
    }));
    const start = pdp.querySelector('.sw[aria-pressed="true"]');
    if (start) paintBlock(pdp, start);
    sync();
  }

  /* ---- cart --------------------------------------------------------------
     Prices in minor units on the row, so the printed line and the total
     come from the same number. */
  const cart = document.getElementById('cart');
  if (cart) {
    const FREE_OVER = 12000;
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
      const ship = units === 0 ? 0 : (sub >= FREE_OVER ? 0 : 495);
      set('sub', money(sub));
      set('ship', units === 0 ? '—' : (ship === 0 ? 'Free' : money(ship)));
      set('total', money(sub + ship));
      set('units', units + (units === 1 ? ' item' : ' items'));
      set('bagcount', String(units));
      const bar = document.getElementById('bar');
      if (bar) bar.style.width = Math.min(100, (sub / FREE_OVER) * 100) + '%';
      const note = document.getElementById('ship-note');
      if (note) note.textContent = units === 0 ? 'Your bag is empty.'
        : sub >= FREE_OVER ? 'Free UK delivery unlocked.'
        : money(FREE_OVER - sub) + ' away from free UK delivery.';
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
