/* ============================================================
   SAN-IN HIDDEN JAPAN — main.js
============================================================ */

(function () {

  // Fade-in
  const fadeEls = document.querySelectorAll('.fade-in');
  if (fadeEls.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
    }, { threshold: 0.08 });
    fadeEls.forEach(el => io.observe(el));
  }

  // Header scroll effect (transparent → solid)
  const header = document.getElementById('global-header');
  if (header && header.dataset.transparent === 'true') {
    const setSolid = () => {
      header.style.background = 'rgba(242, 239, 231, 0.97)';
      header.style.color = '#1B1B19';
      header.classList.add('is-solid');
      // nav links color
      header.querySelectorAll('.header-nav a').forEach(a => a.style.color = '');
      // hamburger color
      const toggle = header.querySelector('.menu-toggle');
      if (toggle) toggle.style.color = '#1B1B19';
    };
    const setTransparent = () => {
      header.style.background = 'transparent';
      header.style.color = '#fff';
      header.classList.remove('is-solid');
      header.querySelectorAll('.header-nav a').forEach(a => a.style.color = '#fff');
      const toggle = header.querySelector('.menu-toggle');
      if (toggle) toggle.style.color = '#fff';
    };
    window.addEventListener('scroll', () => {
      window.scrollY > 60 ? setSolid() : setTransparent();
    }, { passive: true });
  }

  // Hamburger menu
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
      toggle.getAttribute('aria-expanded') === 'true' ? closeMenu() : openMenu();
    });
    closeBtn && closeBtn.addEventListener('click', closeMenu);
    mobileMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileMenu.classList.contains('is-open')) closeMenu();
    });
  }

})();
