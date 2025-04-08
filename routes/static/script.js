document.addEventListener('DOMContentLoaded', () => {
    const routeItems = document.querySelectorAll('.route-item');
    const paths = document.querySelectorAll('svg path[data-id]');
    const cartCountEl = document.querySelector('.cart-count');

    let cart = [];

    // Восстановим из localStorage
    if (localStorage.getItem('cart')) {
        cart = JSON.parse(localStorage.getItem('cart'));
        updateCartCount();
    }

    function updateCartCount() {
        cartCountEl.textContent = cart.length;
    }

    function addToCart(id, title, details) {
        const exists = cart.find(item => item.id === id);
        if (exists) return;

        cart.push({ id, title, details });
        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartCount();
    }

    // Наведение на список
    routeItems.forEach(item => {
        const id = item.dataset.id;

        // Подсветка дуги при наведении на список
        item.addEventListener('mouseenter', () => highlightPath(id));
        item.addEventListener('mouseleave', () => resetPath(id));

        // Добавление в корзину при клике на кнопку
        const btn = item.querySelector('.route-pay-btn');
        if (btn) {
            const title = item.querySelector('.route-title')?.textContent.trim();
            const details = item.querySelector('.route-details')?.textContent.trim();

            btn.addEventListener('click', () => {
                addToCart(id, title, details);
            });
        }
    });

    // Наведение на SVG-сегменты
    paths.forEach(path => {
        const id = path.dataset.id;

        path.addEventListener('mouseenter', () => {
            path.setAttribute('stroke-width', '24');
            const item = document.querySelector(`.route-item[data-id="${id}"]`);
            if (item) item.classList.add('hovered');
        });

        path.addEventListener('mouseleave', () => {
            path.setAttribute('stroke-width', '16');
            const item = document.querySelector(`.route-item[data-id="${id}"]`);
            if (item) item.classList.remove('hovered');
        });
    });

    function highlightPath(id) {
        const path = document.querySelector(`svg path[data-id="${id}"]`);
        if (path) {
            path.setAttribute('stroke-width', '24');
        }
    }

    function resetPath(id) {
        const path = document.querySelector(`svg path[data-id="${id}"]`);
        if (path) {
            path.setAttribute('stroke-width', '16');
        }
    }
});
