/* ══════════════════════════════════════════════════════
   MERA LAUNDRY — Hamburger / Mobile Menu Toggle
   ══════════════════════════════════════════════════════ */

(function () {
  'use strict';

  const hamburger  = document.getElementById('hamburger-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const mobileLinks = mobileMenu ? mobileMenu.querySelectorAll('.mobile-link') : [];

  if (!hamburger || !mobileMenu) return;

  /** Open / Close the mobile menu */
  function toggleMenu(forceClose = false) {
    const isOpen = hamburger.classList.contains('is-open');

    if (forceClose || isOpen) {
      hamburger.classList.remove('is-open');
      mobileMenu.classList.remove('is-open');
      hamburger.setAttribute('aria-expanded', 'false');
      mobileMenu.setAttribute('aria-hidden', 'true');
    } else {
      hamburger.classList.add('is-open');
      mobileMenu.classList.add('is-open');
      hamburger.setAttribute('aria-expanded', 'true');
      mobileMenu.setAttribute('aria-hidden', 'false');
    }
  }

  /* Toggle on button click */
  hamburger.addEventListener('click', () => toggleMenu());

  /* Close on any mobile link click */
  mobileLinks.forEach(link => {
    link.addEventListener('click', () => toggleMenu(true));
  });

  /* Close on outside click / tap */
  document.addEventListener('click', (e) => {
    const navbar = document.querySelector('.navbar');
    if (navbar && !navbar.contains(e.target)) {
      toggleMenu(true);
    }
  });

  /* Close on Escape key */
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') toggleMenu(true);
  });

  /* Close if viewport widens above breakpoint */
  const mq = window.matchMedia('(min-width: 769px)');
  mq.addEventListener('change', (e) => {
    if (e.matches) toggleMenu(true);
  });
})();
// Premium Antigravity Levitation Effect
gsap.to(".premium-washer-wrapper", {
    y: "-=20",             // Floats up 20 pixels
    duration: 3,           // Takes 3 seconds to float up
    ease: "sine.inOut",    // Buttery smooth ease (like real breathing/floating)
    yoyo: true,            // Automatically floats back down
    repeat: -1             // Repeats infinitely
});