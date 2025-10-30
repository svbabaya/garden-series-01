// Get elements
const feedbackBtn = document.querySelector('.feedback-btn');
const feedbackModal = document.getElementById('feedbackModal');
const modalClose = document.querySelector('.modal-close');
const modalOverlay = document.querySelector('.modal-overlay');
const feedbackForm = document.querySelector('.feedback-form');

// Open modal window
feedbackBtn.addEventListener('click', () => {
    feedbackModal.classList.add('show');
    document.body.style.overflow = 'hidden';
});

// Close modal window
function closeModal() {
    feedbackModal.classList.remove('show');
    document.body.style.overflow = '';
}

modalClose.addEventListener('click', closeModal);
modalOverlay.addEventListener('click', closeModal);

// Close by ESC
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && feedbackModal.classList.contains('show')) {
        closeModal();
    }
});

// Handler of sending
feedbackForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form data
    const formData = new FormData(feedbackForm);
    const data = Object.fromEntries(formData);

    // Send data to server
    console.log('Form data:', data);

    // Success message
    alert('Message sent');

    // Close modal and reset form
    closeModal();
    feedbackForm.reset();
});

// Preventing content from closing when clicking on it
document.querySelector('.modal-content').addEventListener('click', (e) => {
    e.stopPropagation();
});
