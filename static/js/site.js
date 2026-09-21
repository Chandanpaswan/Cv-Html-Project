document.addEventListener('DOMContentLoaded', () => {
    const navToggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links');
    if (navToggle && navLinks) {
        navToggle.addEventListener('click', () => {
            const open = navLinks.classList.toggle('open');
            navToggle.setAttribute('aria-expanded', open);
            navToggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
        });
        navLinks.querySelectorAll('a').forEach(link => link.addEventListener('click', () => navLinks.classList.remove('open')));
    }

    document.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click', () => {
        document.querySelectorAll('[data-filter]').forEach(item => item.classList.remove('active'));
        button.classList.add('active');
        const selected = button.dataset.filter;
        document.querySelectorAll('.project-card').forEach(card => { card.hidden = selected !== 'all' && card.dataset.category !== selected; });
    }));

    const observer = 'IntersectionObserver' in window ? new IntersectionObserver(entries => entries.forEach(entry => {
        if (entry.isIntersecting) entry.target.classList.add('is-visible');
    }), { threshold: 0.12 }) : null;
    document.querySelectorAll('.reveal').forEach(element => observer ? observer.observe(element) : element.classList.add('is-visible'));

    const backTop = document.querySelector('.back-top');
    if (backTop) {
        window.addEventListener('scroll', () => backTop.classList.toggle('visible', window.scrollY > 600), { passive: true });
        backTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
    }

    const printButton = document.querySelector('#download-cv');
    if (printButton) printButton.addEventListener('click', () => window.print());
});
