/* ==========================================================================
   Nocturne — one script for every page. Each block looks for its own hooks
   and does nothing if they are not on the page, so the same file can be
   included everywhere without branching on the filename.
   ========================================================================== */
(() => {
  const $  = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const money = n => '$' + n.toFixed(2);

  /* ---- announcement ticker ---------------------------------------------
     Rotates on its own and on the arrows. The timer restarts whenever
     somebody clicks, so a message they chose is not whipped away. */
  const tick = $('#tick');
  if (tick) {
    const lines = [
      'Autumn pieces are up — free shipping over $120',
      'Everything is printed by hand in Atlanta',
      'Runs of fifty, numbered, never reprinted',
    ];
    let i = 0, timer;
    const show = () => { tick.textContent = lines[((i % lines.length) + lines.length) % lines.length]; };
    const start = () => { clearInterval(timer); timer = setInterval(() => { i++; show(); }, 5200); };
    $$('[data-tick]').forEach(b => b.addEventListener('click', () => {
      i += Number(b.dataset.tick); show(); start();
    }));
    show(); start();
  }

  /* ---- collections dropdown --------------------------------------------- */
  $$('[data-drop]').forEach(drop => {
    const btn = drop.querySelector('button');
    const set = open => {
      drop.dataset.open = String(open);
      btn.setAttribute('aria-expanded', String(open));
    };
    btn.addEventListener('click', e => {
      e.stopPropagation();
      set(drop.dataset.open !== 'true');
    });
    drop.addEventListener('mouseleave', () => set(false));
    document.addEventListener('click', () => set(false));
    document.addEventListener('keydown', e => { if (e.key === 'Escape') set(false); });
  });

  /* ---- mobile drawer ---------------------------------------------------- */
  const drawer = $('[data-drawerpanel]'), scrim = $('[data-scrim]'), burger = $('[data-drawer]');
  if (drawer && burger) {
    const set = open => {
      drawer.dataset.open = String(open);
      scrim.dataset.open  = String(open);
      burger.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
    };
    burger.addEventListener('click', () => set(drawer.dataset.open !== 'true'));
    scrim.addEventListener('click', () => set(false));
    $('[data-drawerclose]')?.addEventListener('click', () => set(false));
    document.addEventListener('keydown', e => { if (e.key === 'Escape') set(false); });
  }

  /* ---- the standing offer tab ------------------------------------------- */
  const offer = $('[data-offer]');
  if (offer) {
    const t = $('[data-offer-toggle]', offer);
    t.addEventListener('click', () => {
      const open = offer.dataset.open !== 'true';
      offer.dataset.open = String(open);
      t.setAttribute('aria-expanded', String(open));
    });
  }

  /* ---- colour swatches ---------------------------------------------------
     The swatch owns the colour class. Clicking it repaints every garment
     inside the same block, so the artwork and the printed colour name can
     never disagree, and it carries which sizes are gone in that colour. */
  const COLOURS = ['g-bone','g-black','g-ink','g-ash','g-sky','g-red','g-navy','g-sand'];
  const paint = (block, btn, targets) => {
    const cls = btn.dataset.swatch;
    block.querySelectorAll('[data-swatch]').forEach(o => {
      if (o.parentElement === btn.parentElement) o.setAttribute('aria-pressed', String(o === btn));
    });
    (targets || block.querySelectorAll('.gar')).forEach(g => {
      COLOURS.forEach(c => g.classList.remove(c));
      g.classList.add(cls);
    });
  };

  $$('.card').forEach(card => {
    const plate = card.querySelector('.shot .gar');
    card.querySelectorAll('.sw').forEach(btn => {
      btn.addEventListener('click', e => { e.preventDefault(); paint(card, btn, plate ? [plate] : []); });
    });
  });

  /* ---- collection filter and sort ---------------------------------------
     The category can arrive in the URL, because the Collections menu links
     straight to one. The heading and the note follow it, so a visitor who
     lands on ?c=sweats sees a Sweats page rather than "Collections". */
  const grid = $('#grid');
  if (grid) {
    const cards = $$('.card', grid);
    const chips = $$('.chip');
    const sort  = $('#sort');
    const count = $('#count');
    const empty = $('#empty');
    const title = $('#colltitle');
    const note  = $('#collnote');
    const NAMES = {
      all:    ['Collections', 'Nine pieces, cut this season. Everything is unisex and everything is printed by hand, so no two are quite the same.'],
      shirts: ['Shirts', 'Short and long sleeve, 6.5oz cotton, printed one colour at a time.'],
      sweats: ['Sweats', 'Heavyweight fleece, brushed inside, cut to sit square on the shoulder.'],
      sets:   ['Sets', 'Bought together and cut together, so the dye lot actually matches.'],
      extras: ['Extras', 'The small things. Knitted and embroidered rather than printed.'],
    };
    let cat = 'all';

    const render = () => {
      let shown = 0;
      cards.forEach(c => {
        const hit = cat === 'all' || c.dataset.cat === cat;
        c.hidden = !hit;
        if (hit) shown++;
      });
      if (count) count.textContent = shown + (shown === 1 ? ' piece' : ' pieces');
      if (empty) empty.hidden = shown !== 0;

      const mode = sort ? sort.value : 'feat';
      const live = cards.filter(c => !c.hidden).sort((a, b) => {
        if (mode === 'lo') return a.dataset.price - b.dataset.price;
        if (mode === 'hi') return b.dataset.price - a.dataset.price;
        if (mode === 'az') return a.dataset.name.localeCompare(b.dataset.name);
        return a.dataset.rank - b.dataset.rank;
      });
      live.forEach(c => grid.appendChild(c));

      chips.forEach(ch => ch.setAttribute('aria-pressed', String(ch.dataset.cat === cat)));
      const [h, p] = NAMES[cat] || NAMES.all;
      if (title) title.textContent = h;
      if (note)  note.textContent  = p;
    };

    chips.forEach(ch => ch.addEventListener('click', () => {
      cat = ch.dataset.cat;
      history.replaceState(null, '', cat === 'all' ? location.pathname : '?c=' + cat);
      render();
    }));
    sort?.addEventListener('change', render);

    const fromUrl = new URLSearchParams(location.search).get('c');
    if (fromUrl && NAMES[fromUrl]) cat = fromUrl;
    render();
  }

  /* ---- product page ------------------------------------------------------ */
  const pdp = $('#pdp');
  if (pdp) {
    const stage   = $('#stage');
    const thumbs  = $$('[data-thumbs] button');
    const frameno = $('#frameno');
    const cname   = $('#cname');
    const sizes   = $$('[data-opt="size"] .pill');
    const colours = $$('[data-opt="colour"] .pill');

    const setColour = (cls, name, gone) => {
      COLOURS.forEach(c => stage.classList.remove(c));
      stage.classList.add(cls);
      if (cname) cname.textContent = name;
      thumbs.forEach((t, n) => {
        const on = t.dataset.swatch === cls;
        t.setAttribute('aria-pressed', String(on));
        if (on && frameno) frameno.textContent = (n + 1) + ' / ' + thumbs.length;
      });
      /* Sold-out sizes are a property of the colour, so they are reapplied
         every time the colour changes rather than set once on load. */
      const out = (gone || '').split(',').map(s => s.trim()).filter(Boolean);
      sizes.forEach(s => {
        const dead = out.includes(s.dataset.size);
        s.disabled = dead;
        if (dead && s.getAttribute('aria-pressed') === 'true') {
          s.setAttribute('aria-pressed', 'false');
          const first = sizes.find(o => !o.disabled);
          first?.setAttribute('aria-pressed', 'true');
        }
      });
    };

    colours.forEach(btn => btn.addEventListener('click', () => {
      colours.forEach(o => o.setAttribute('aria-pressed', String(o === btn)));
      setColour(btn.dataset.swatch, btn.dataset.name, btn.dataset.gone);
    }));

    thumbs.forEach(t => t.addEventListener('click', () => {
      const match = colours.find(c => c.dataset.swatch === t.dataset.swatch);
      if (match) { match.click(); return; }
      COLOURS.forEach(c => stage.classList.remove(c));
      stage.classList.add(t.dataset.swatch);
      thumbs.forEach((o, n) => {
        o.setAttribute('aria-pressed', String(o === t));
        if (o === t && frameno) frameno.textContent = (n + 1) + ' / ' + thumbs.length;
      });
    }));

    sizes.forEach(btn => btn.addEventListener('click', () => {
      if (btn.disabled) return;
      sizes.forEach(o => o.setAttribute('aria-pressed', String(o === btn)));
    }));

    const start = colours.find(c => c.getAttribute('aria-pressed') === 'true');
    if (start) setColour(start.dataset.swatch, start.dataset.name, start.dataset.gone);

    const note = $('#addnote');
    const add = () => {
      const size   = sizes.find(s => s.getAttribute('aria-pressed') === 'true')?.dataset.size || 'Medium';
      const colour = colours.find(c => c.getAttribute('aria-pressed') === 'true')?.dataset.name || 'Bone';
      const cls    = colours.find(c => c.getAttribute('aria-pressed') === 'true')?.dataset.swatch || 'g-bone';
      Bag.add({ name: 'Second Feature Tee', variant: colour + ' · ' + size, price: 60, cls, shape: 'tee', print: 'Second Feature' });
      if (note) note.textContent = 'Second Feature Tee, ' + colour + ', ' + size + ' — added to the cart.';
    };
    $('#addcart')?.addEventListener('click', add);
    $('#buynow')?.addEventListener('click', () => {
      add();
      if (note) note.textContent = 'This is a demo copy, so there is no checkout to send you to. The piece is in the cart.';
    });
  }

  /* ---- the bag -----------------------------------------------------------
     sessionStorage, not localStorage: a demo cart that is still full three
     weeks later is confusing, and the whole point of this copy is that
     nothing it holds survives being useful for one visit. Wrapped because
     storage throws outright in a private window. */
  const KEY = 'nocturne-bag';
  const Bag = {
    read() {
      try { return JSON.parse(sessionStorage.getItem(KEY)) || null; } catch (e) { return null; }
    },
    write(items) {
      try { sessionStorage.setItem(KEY, JSON.stringify(items)); } catch (e) { /* no storage, memory only */ }
      Bag.mem = items;
      Bag.badge();
    },
    items() {
      if (Bag.mem) return Bag.mem;
      const stored = Bag.read();
      Bag.mem = stored || [
        { name: 'Second Feature Tee', variant: 'Bone · Medium', price: 60, qty: 1, cls: 'g-bone', shape: 'tee', print: 'Second Feature' },
        { name: 'Nocturne Beanie',    variant: 'Navy · One size', price: 25, qty: 1, cls: 'g-navy', shape: 'beanie', print: 'N' },
      ];
      return Bag.mem;
    },
    add(line) {
      const items = Bag.items();
      const hit = items.find(i => i.name === line.name && i.variant === line.variant);
      if (hit) hit.qty += 1; else items.push({ ...line, qty: 1 });
      Bag.write(items);
      Bag.render();
    },
    badge() {
      const n = (Bag.mem || []).reduce((t, i) => t + i.qty, 0);
      $$('[data-bagcount]').forEach(el => { el.textContent = n; el.hidden = n === 0; });
    },
    render() {
      const lines = $('#lines');
      if (!lines) return;
      const items = Bag.items();
      lines.innerHTML = '';
      items.forEach((it, idx) => {
        const row = document.createElement('div');
        row.className = 'line';
        row.innerHTML =
          '<span class="thumb"><span class="gar ' + it.shape + ' ' + it.cls + '" data-print="' + it.print + '" aria-hidden="true"></span></span>' +
          '<div><p class="nm">' + it.name + '</p><p class="vr">' + it.variant + '</p>' +
          '<button class="rm" type="button" data-rm="' + idx + '">Remove</button></div>' +
          '<div style="text-align:right"><p class="num">' + money(it.price * it.qty) + '</p>' +
          '<span class="qty"><button type="button" data-q="-1" data-i="' + idx + '" aria-label="One fewer">–</button>' +
          '<span class="num">' + it.qty + '</span>' +
          '<button type="button" data-q="1" data-i="' + idx + '" aria-label="One more">+</button></span></div>';
        lines.appendChild(row);
      });
      const sub = items.reduce((t, i) => t + i.price * i.qty, 0);
      $('#sub') && ($('#sub').textContent = money(sub));
      $('#tot') && ($('#tot').textContent = money(sub));
      $('#cartempty') && ($('#cartempty').hidden = items.length > 0);
      $('#sums') && ($('#sums').hidden = items.length === 0);
      Bag.badge();
    },
  };

  $('#lines')?.addEventListener('click', e => {
    const q = e.target.closest('[data-q]');
    const r = e.target.closest('[data-rm]');
    const items = Bag.items();
    if (q) {
      const i = Number(q.dataset.i);
      items[i].qty = Math.max(0, items[i].qty + Number(q.dataset.q));
      if (items[i].qty === 0) items.splice(i, 1);
    } else if (r) {
      items.splice(Number(r.dataset.rm), 1);
    } else return;
    Bag.write(items);
    Bag.render();
  });

  $('#checkout')?.addEventListener('click', () => {
    const n = $('#checknote');
    if (n) n.textContent = 'This is a demo copy of a site we built, so checkout is switched off. On the live store this is where Shopify takes over.';
  });

  Bag.items();
  Bag.badge();
  Bag.render();
})();
