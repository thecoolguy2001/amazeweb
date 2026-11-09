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

  /* Reveal-on-scroll, mirroring the entrance fades on the published site */
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window) {
    var targets = document.querySelectorAll('.scard, .svc, .tpl-card, .faq-group, .theme-note, .theme-more a, .form-card');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    targets.forEach(function (t) { t.classList.add('reveal'); io.observe(t); });
  }
})();
