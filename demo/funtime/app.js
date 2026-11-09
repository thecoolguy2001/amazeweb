(() => {
  const head = document.getElementById('masthead');
  if (head) {
    const onScroll = () => head.classList.toggle('is-stuck', window.scrollY > 8);
    onScroll();
    addEventListener('scroll', onScroll, {passive:true});
  }

  /* One age filter, two targets. Parents arrive with exactly one question --
     "what is there for a five year old?" -- so the control drives the
     programs grid and the timetable together rather than making them pick
     an age twice on two different pages. Each item lists the bands it
     belongs to in data-ages, space separated. */
  const bar = document.getElementById('agebar');
  if (!bar) return;

  const buttons = Array.from(bar.querySelectorAll('.age'));
  const items   = Array.from(document.querySelectorAll('[data-ages]'));
  const shown   = document.getElementById('shown');

  const apply = (band) => {
    let n = 0;
    items.forEach(el => {
      const hit = band === 'all' || el.dataset.ages.split(' ').includes(band);
      el.hidden = !hit;
      if (hit && el.classList.contains('prog')) n++;
    });
    if (shown) {
      const label = band === 'all' ? 'all ages'
                  : buttons.find(b => b.dataset.age === band).textContent.trim();
      shown.textContent = n + (n === 1 ? ' program' : ' programs') + ' for ' + label;
    }
  };

  buttons.forEach(b => b.addEventListener('click', () => {
    buttons.forEach(o => o.setAttribute('aria-pressed', String(o === b)));
    apply(b.dataset.age);
  }));
  apply('all');
})();
