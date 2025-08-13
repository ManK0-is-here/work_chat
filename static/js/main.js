document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM fully loaded and parsed');
    
    // Элементы модального окна входа
    const loginModal = document.getElementById('login-modal');
    const closeModal = document.querySelector('.close-modal');
    const loginBtns = document.querySelectorAll('.login-btn');
    
    // Функция открытия/закрытия модального окна
    function toggleLoginModal(show) {
        if (show) {
            loginModal.style.display = 'flex';
            document.body.style.overflow = 'hidden';
        } else {
            loginModal.style.display = 'none';
            document.body.style.overflow = '';
        }
    }
    
    // Открытие модалки по клику на "Войти"
    if (loginBtns.length > 0) {
        loginBtns.forEach(btn => {
            btn.addEventListener('click', () => toggleLoginModal(true));
        });
    }
    
    // Закрытие модалки
    if (closeModal) {
        closeModal.addEventListener('click', () => toggleLoginModal(false));
    }
    
    // Закрытие по клику вне модалки
    if (loginModal) {
        loginModal.addEventListener('click', (e) => {
            if (e.target === loginModal) toggleLoginModal(false);
        });
    }
    
    // Закрытие по ESC
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && loginModal.style.display === 'flex') {
            toggleLoginModal(false);
        }
    });
});