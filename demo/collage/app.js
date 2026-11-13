/* ==========================================================================
   Collage — one script for every page.
   The only real interaction is the lightbox: a portfolio is read in order
   more often than it is clicked around, so the arrow keys move along the
   row and the dialog says where you are in it.
   ========================================================================== */
(() => {
  const $  = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));

  const box = $('[data-box]');
  if (!box) return;

  const pieces = $$('[data-piece]');
  if (!pieces.length) return;

  const face  = $('[data-boxface]', box);
  const title = $('[data-boxtitle]', box);
  const note  = $('[data-boxnote]', box);
  const meta  = $('[data-boxmeta]', box);
  const of    = $('[data-boxof]', box);
  const SWATCHES = ['p1','p2','p3','p4','p5','p6','p7','p8','p9'];
  const LAYS = ['lay-a','lay-b','lay-c','lay-d'];

  let at = 0;
  let opener = null;

  const show = i => {
    at = (i + pieces.length) % pieces.length;
    const p = pieces[at];
    SWATCHES.forEach(c => face.classList.remove(c));
    LAYS.forEach(c => face.classList.remove(c));
    face.classList.add(p.dataset.swatch);
    if (p.dataset.lay) face.classList.add(p.dataset.lay);
    title.textContent = p.dataset.title;
    note.textContent  = p.dataset.note;
    meta.textContent  = p.dataset.meta;
    of.textContent    = (at + 1) + ' of ' + pieces.length;
  };

  const open = i => {
    opener = pieces[i];
    show(i);
    box.dataset.open = 'true';
    box.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    $('[data-boxnext]', box)?.focus();
  };

  const shut = () => {
    box.dataset.open = 'false';
    box.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    opener?.focus();
  };

  pieces.forEach((p, i) => p.addEventListener('click', () => open(i)));
  $('[data-boxclose]', box)?.addEventListener('click', shut);
  $('[data-boxprev]', box)?.addEventListener('click', () => show(at - 1));
  $('[data-boxnext]', box)?.addEventListener('click', () => show(at + 1));

  /* Clicking the backdrop closes; clicking the card itself does not. */
  box.addEventListener('click', e => { if (e.target === box) shut(); });

  document.addEventListener('keydown', e => {
    if (box.dataset.open !== 'true') return;
    if (e.key === 'Escape')     { shut(); }
    if (e.key === 'ArrowRight') { show(at + 1); }
    if (e.key === 'ArrowLeft')  { show(at - 1); }
  });
})();
