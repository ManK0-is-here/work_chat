// static/js/script.js
// Анимация навигации при скролле
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.style.backgroundColor = 'rgba(10, 10, 10, 0.9)';
        navbar.style.padding = '1rem 5%';
    } else {
        navbar.style.backgroundColor = 'transparent';
        navbar.style.padding = '2rem 5%';
    }
});

// Плавная прокрутка для якорных ссылок
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Инициализация фонового видео (если используется)
const initVideoBackground = () => {
    const videoBg = document.querySelector('.video-background');
    if (videoBg) {
        const video = videoBg.querySelector('video');
        video.play().catch(error => {
            console.log('Автовоспроизведение видео заблокировано:', error);
        });
    }
};

// Запуск при загрузке страницы
document.addEventListener('DOMContentLoaded', () => {
    initVideoBackground();
});