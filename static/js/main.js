document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM fully loaded and parsed');
    
    // Элементы модального окна
    const registerModal = document.getElementById('register-modal');
    const closeModal = document.querySelector('.close-modal');
    const registerBtns = document.querySelectorAll('.register-btn');
    
    // Проверка существования элементов
    if (!registerModal) console.error('Modal element not found!');
    if (!closeModal) console.error('Close button not found!');
    if (registerBtns.length === 0) console.warn('Register buttons not found');
    
    // Функция открытия/закрытия модального окна
    function toggleModal(show) {
        if (!registerModal) return;
        
        if (show) {
            registerModal.style.display = 'flex';
            document.body.style.overflow = 'hidden';
        } else {
            registerModal.style.display = 'none';
            document.body.style.overflow = '';
        }
    }
    
    if (registerBtns.length > 0) {
        registerBtns.forEach(btn => {
            btn.addEventListener('click', () => toggleModal(true));
        });
    }
    
    if (closeModal) {
        closeModal.addEventListener('click', () => toggleModal(false));
    }
    
    if (registerModal) {
        registerModal.addEventListener('click', (e) => {
            if (e.target === registerModal) toggleModal(false);
        });
    }
    
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && registerModal.style.display === 'flex') {
            toggleModal(false);
        }
    });
})