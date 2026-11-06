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
