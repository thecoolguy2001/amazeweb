/* Amazé Web — behaviour */
(function () {
  'use strict';

  /* FAQ accordion, one group open at a time (as on the published site).
     Framer collapses the group row with overflow:hidden and height 96px ->
     min-content, and the answers inside start at opacity 0 (its closed SSR
     markup carries `opacity:0;transform:none`, so it is a fade, not a slide).
     <details> cannot transition to height:auto across browsers, so the height
     is driven in pixels here and handed back to auto once it settles. */
  var groups = Array.prototype.slice.call(document.querySelectorAll('.faq-group'));
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  groups.forEach(function (g) {
    var panel = g.querySelector('.faq-panel');
    var head = g.querySelector('.faq-head');
    if (!panel || !head) return;

    if (reduceMotion) {                        /* native open, no height animation */
      g.addEventListener('toggle', function () {
        if (!g.open) return;
        groups.forEach(function (o) { if (o !== g) o.open = false; });
      });
      return;
    }

    g.classList.add('anim');
    var run = 0;                               /* cancels callbacks from a superseded run */

    function settle(token, fn) {
      var timer;
      var done = function (e) {
        if (e && e.propertyName !== 'height') return;
        panel.removeEventListener('transitionend', done);
        clearTimeout(timer);
        if (token === run) fn();
      };
      timer = setTimeout(done, 520);           /* in case transitionend never fires */
      panel.addEventListener('transitionend', done);
    }

    function expand() {
      var token = ++run;
      g.classList.remove('closing');
      g.open = true;
      panel.style.height = '0px';
      panel.style.height = panel.scrollHeight + 'px';   /* the read commits the 0 */
      settle(token, function () { panel.style.height = 'auto'; });
    }

    function collapse() {
      var token = ++run;
      g.classList.add('closing');
      panel.style.height = panel.scrollHeight + 'px';
      void panel.offsetHeight;                 /* commit the pixel height */
      panel.style.height = '0px';
      settle(token, function () {
        g.open = false;
        g.classList.remove('closing');
        panel.style.height = '';
      });
    }

    g.collapseGroup = collapse;

    head.addEventListener('click', function (e) {
      e.preventDefault();                      /* drive `open` ourselves */
      if (g.open && !g.classList.contains('closing')) { collapse(); return; }
      groups.forEach(function (o) {
        if (o !== g && o.open && o.collapseGroup && !o.classList.contains('closing')) {
          o.collapseGroup();
        }
      });
      expand();
    });
  });

  /* Back To Top */
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href="#top"]');
    if (!a) return;
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });


  /* Mobile nav: the pill grows to reveal the stacked links (<810px) */
  var pill = document.querySelector('.nav-pill');
  var toggle = pill && pill.querySelector('.nav-toggle');
  if (toggle) {
    var setOpen = function (open) {
      pill.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    };
    toggle.addEventListener('click', function () {
      setOpen(!pill.classList.contains('open'));
    });
    /* close on link tap, on Escape, and on tap outside */
    pill.querySelectorAll('.nav-links a').forEach(function (a) {
      a.addEventListener('click', function () { setOpen(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && pill.classList.contains('open')) { setOpen(false); toggle.focus(); }
    });
    document.addEventListener('click', function (e) {
      if (pill.classList.contains('open') && !pill.contains(e.target)) setOpen(false);
    });
    /* leaving the phone breakpoint must not strand it open */
    var mq = window.matchMedia('(min-width: 810px)');
    (mq.addEventListener ? mq.addEventListener.bind(mq, 'change') : mq.addListener.bind(mq))(
      function (e) { if (e.matches) setOpen(false); });
  }

  /* Horizontal rails ("More themes to explore"). The row scrolls and snaps on
     its own; these buttons just give a pointer user something to click. They
     stay hidden until we know the row actually overflows, and each one hides
     again at its end of the track. */
  Array.prototype.forEach.call(document.querySelectorAll('.rail-wrap'), function (wrap) {
    var rail = wrap.querySelector('.rail');
    var prev = wrap.querySelector('.rail-btn.prev');
    var next = wrap.querySelector('.rail-btn.next');
    if (!rail || !prev || !next) return;

    function step() {
      var card = rail.firstElementChild;
      var gap = parseFloat(getComputedStyle(rail).columnGap) || 24;
      return card ? card.getBoundingClientRect().width + gap : 300;
    }
    function sync() {
      /* 8px of slack: the rail is inset 6px so snapping parks scrollLeft at 6,
         not 0, and the far end lands just short of max. */
      var max = rail.scrollWidth - rail.clientWidth;
      if (max <= 8) { prev.hidden = true; next.hidden = true; return; }
      prev.hidden = rail.scrollLeft <= 8;
      next.hidden = rail.scrollLeft >= max - 8;
    }
    prev.addEventListener('click', function () { rail.scrollLeft -= step(); });
    next.addEventListener('click', function () { rail.scrollLeft += step(); });
    rail.addEventListener('scroll', sync, { passive: true });
    window.addEventListener('resize', sync);
    sync();
  });

  /* Reveal-on-scroll, mirroring the entrance fades on the published site */
  var revealSel = '.scard, .svc, .tpl-card, .faq-group, .theme-note, .form-card';
  if (!('IntersectionObserver' in window)) {
    /* The hidden state is in CSS now, so without an observer to clear it the
       page would stay blank. Show everything at once instead. */
    Array.prototype.forEach.call(document.querySelectorAll(revealSel),
      function (el) { el.classList.add('in'); });
  } else if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    /* The hidden state already comes from CSS (html.js ...), so nothing is
       added here -- adding it from this deferred script is what made the page
       fade out after first paint. We only mark elements as they come into
       view. Cards inside a horizontal rail are skipped: the ones off to the
       right never intersect the viewport, so they would sit at opacity 0 until
       you scrolled the rail sideways and then fade UP into place. The CSS
       selector excludes them too -- keep the two lists in step. */
    var targets = Array.prototype.filter.call(
      document.querySelectorAll('.scard, .svc, .tpl-card, .faq-group, .theme-note, .form-card'),
      function (el) { return !el.closest('.rail'); });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    targets.forEach(function (t) { io.observe(t); });
  }
})();
