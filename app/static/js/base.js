/* Notification button */
function closeNotification() {
    var flashNotification = document.getElementById('flash-notification');

    if (flashNotification) {
        flashNotification.style.display = 'none';
    }
}

/* Dropdown list */
const dropdown = document.querySelector('.dropdown');
const active = document.querySelector('.is-active')

document.body.addEventListener('click', function () {
    if (active) {
        dropdown.classList.remove('is-active')
    }
});

dropdown.addEventListener('click', function (event) {
    event.stopPropagation();
    this.classList.toggle('is-active');
});

/* Logout form button */
function logout() {
    document.getElementById('logoutForm').submit();
}