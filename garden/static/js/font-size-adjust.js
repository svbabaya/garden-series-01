function updateFontFromFooterHeight() {
    const footerTape = document.getElementById('footerTape');
    if (!footerTape) return;
    const footerHeight = footerTape.offsetHeight;
    const fontSize = footerHeight * 0.4;
    document.documentElement.style.setProperty('--font-size-from-footer', `${fontSize}px`);
}

document.addEventListener('DOMContentLoaded', function() {
    updateFontFromFooterHeight();
});

window.addEventListener('resize', updateFontFromFooterHeight);

if ('ResizeObserver' in window) {
    const observer = new ResizeObserver(updateFontFromFooterHeight);
    document.addEventListener('DOMContentLoaded', function() {
        const footerTape = document.getElementById('footerTape');
        if (footerTape) {
            observer.observe(footerTape);
        }
    });
}
