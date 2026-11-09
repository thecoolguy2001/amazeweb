(() => {
  const head = document.getElementById('masthead');
  if (head) {
    const onScroll = () => head.classList.toggle('is-stuck', window.scrollY > 8);
    onScroll();
    addEventListener('scroll', onScroll, {passive:true});
  }

  /* The day part runs the page. One control switches the menu panel, the
     service hours shown beside it, and the booking slots further down, so
     lunch and dinner never have to be two separate pages. */
  const tabs = Array.from(document.querySelectorAll('[data-service]'));
  if (tabs.length) {
    const panels = Array.from(document.querySelectorAll('.service'));
    const when   = document.getElementById('when');
    const HOURS  = {lunch:'Wednesday to Saturday, 12:00 – 14:30',
                    dinner:'Wednesday to Saturday, 18:00 – 22:00',
                    sunday:'Sunday, 12:30 – 17:00, one sitting'};
    const set = (name) => {
      panels.forEach(p => { p.hidden = p.dataset.service !== name; });
      if (when) when.textContent = HOURS[name] || '';
      document.querySelectorAll('[data-slots]').forEach(g => {
        g.hidden = g.dataset.slots !== name;
      });
    };
    tabs.forEach(b => b.addEventListener('click', () => {
      tabs.forEach(o => o.setAttribute('aria-pressed', String(o === b)));
      set(b.dataset.service);
    }));
    const start = tabs.find(t => t.getAttribute('aria-pressed') === 'true') || tabs[0];
    set(start.dataset.service);
  }

  /* Booking slots. Picking a time fills the hidden field the form submits,
     so the pretty control and the real input never disagree. */
  const field = document.getElementById('time');
  const note  = document.getElementById('slot-note');
  const slots = Array.from(document.querySelectorAll('.slot'));
  if (field && slots.length) {
    slots.forEach(s => s.addEventListener('click', () => {
      if (s.disabled) return;
      slots.forEach(o => o.setAttribute('aria-pressed', String(o === s)));
      field.value = s.dataset.time;
      if (note) note.innerHTML = 'Holding <b>' + s.dataset.time +
        '</b> — tables are held for ten minutes while you finish the form.';
    }));
  }
})();
