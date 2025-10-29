/* For browsers that do not support :has() */
document.addEventListener('DOMContentLoaded', function() {
    const menuCheckbox = document.getElementById('menu');

    menuCheckbox.addEventListener('change', function() {
        if (this.checked) {
            document.body.classList.add('no-scroll');
        } else {
            document.body.classList.remove('no-scroll');
        }
    });
});
