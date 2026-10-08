(() => {
  const year = document.querySelector('#year');
  if (year) year.textContent = String(new Date().getFullYear());

  const reveals = [...document.querySelectorAll('.reveal')];
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduceMotion || !('IntersectionObserver' in window)) {
    reveals.forEach((node) => node.classList.add('in-view'));
  } else {
    const observer = new IntersectionObserver((entries, currentObserver) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('in-view');
        currentObserver.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -36px 0px' });
    reveals.forEach((node) => observer.observe(node));
  }

  const hero = document.querySelector('.hero');
  if (hero && 'IntersectionObserver' in window) {
    new IntersectionObserver(([entry]) => {
      hero.classList.toggle('is-paused', !entry.isIntersecting);
    }).observe(hero);
  }

  document.querySelectorAll('.project-gallery').forEach((gallery) => {
    const buttons = [...gallery.querySelectorAll('[data-view]')];
    const images = [...gallery.querySelectorAll(':scope > img')];
    buttons.forEach((button) => {
      button.addEventListener('click', () => {
        const view = Number(button.dataset.view);
        buttons.forEach((other) => other.setAttribute('aria-pressed', String(other === button)));
        if (images[view].dataset.src) {
          images[view].src = images[view].dataset.src;
          images[view].removeAttribute('data-src');
        }
        images.forEach((image, index) => { image.hidden = index !== view; });
      });
    });
  });

  const menu = document.querySelector('.mobile-menu');
  menu?.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => { menu.open = false; });
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && menu?.open) {
      menu.open = false;
      menu.querySelector('summary')?.focus();
    }
  });
})();
