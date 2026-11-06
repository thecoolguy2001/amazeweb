/* Amazé Web — behaviour */
(function () {
  'use strict';

  /* FAQ: one group open at a time (matches the Framer accordion) */
  var groups = Array.prototype.slice.call(document.querySelectorAll('.faq-group'));
  groups.forEach(function (g) {
    g.addEventListener('toggle', function () {
      if (!g.open) return;
      groups.forEach(function (o) { if (o !== g) o.open = false; });
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
