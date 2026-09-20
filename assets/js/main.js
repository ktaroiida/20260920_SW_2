document.addEventListener('DOMContentLoaded', () => {
  // Simple form handling
  const forms = document.querySelectorAll('.early-access-form');
  
  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const messageEl = form.nextElementSibling;
      if (messageEl && messageEl.classList.contains('form-message')) {
        form.style.display = 'none';
        messageEl.style.display = 'block';
        messageEl.textContent = 'ご登録ありがとうございます。';
      }
    });
  });

  // Intersection Observer for simple fade-in animations
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  const fadeElements = document.querySelectorAll('.fade-in');
  fadeElements.forEach(el => observer.observe(el));
});
