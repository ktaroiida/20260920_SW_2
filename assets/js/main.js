/* ============================================================
   SAN-IN HIDDEN JAPAN — main.js
============================================================ */

(function () {

  // ──────────────────────────────
  // Fade-in (IntersectionObserver)
  // ──────────────────────────────
  const fadeEls = document.querySelectorAll('.fade-in');
  if (fadeEls.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) e.target.classList.add('visible');
      });
    }, { threshold: 0.08 });
    fadeEls.forEach(el => io.observe(el));
  }

  // ──────────────────────────────
  // Header scroll effect
  // ──────────────────────────────
  const header = document.getElementById('global-header');
  if (header) {
    const isTransparent = header.dataset.transparent === 'true';
    if (isTransparent) {
      const onScroll = () => {
        if (window.scrollY > 60) {
          header.style.background = 'rgba(242, 239, 231, 0.97)';
          header.style.color = '#1B1B19';
          header.querySelectorAll('a').forEach(a => a.style.color = '');
        } else {
          header.style.background = 'transparent';
          header.style.color = '#fff';
          header.querySelectorAll('a').forEach(a => a.style.color = '#fff');
        }
      };
      window.addEventListener('scroll', onScroll, { passive: true });
    }
  }

  // ──────────────────────────────
  // Hamburger menu
  // ──────────────────────────────
  const toggle = document.querySelector('.menu-toggle');
  const mobileMenu = document.querySelector('.mobile-menu');
  const closeBtn = document.querySelector('.mobile-menu-close');

  function openMenu() {
    mobileMenu.classList.add('is-open');
    mobileMenu.setAttribute('aria-hidden', 'false');
    toggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
    closeBtn && closeBtn.focus();
  }

  function closeMenu() {
    mobileMenu.classList.remove('is-open');
    mobileMenu.setAttribute('aria-hidden', 'true');
    toggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    toggle && toggle.focus();
  }

  if (toggle && mobileMenu) {
    toggle.addEventListener('click', () => {
      const isOpen = toggle.getAttribute('aria-expanded') === 'true';
      isOpen ? closeMenu() : openMenu();
    });

    closeBtn && closeBtn.addEventListener('click', closeMenu);

    // Close on nav link click
    mobileMenu.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', closeMenu);
    });

    // ESC key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileMenu.classList.contains('is-open')) closeMenu();
    });
  }

})();
