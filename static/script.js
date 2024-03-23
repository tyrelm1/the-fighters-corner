document.addEventListener("DOMContentLoaded", function() {
    // Signup form submission
    document.getElementById("signup-form").addEventListener("submit", function(event) {
        var password1 = document.getElementById("id_password1").value;
        var password2 = document.getElementById("id_password2").value;

        if (password1.length < 8 || password2.length < 8) {
            event.preventDefault(); // Prevent form submission
            document.getElementById("password-requirements").style.display = "block"; // Show password requirements message
        }
    });

    // RSVP form submission
    var rsvpForm = document.getElementById('rsvpForm');
    if (rsvpForm) {
        rsvpForm.addEventListener('submit', function() {
            showAlert();  // Call the showAlert function when the form is submitted
        });
    }

    // Comment edit form submission
    var commentEditForm = document.getElementById('comment_edit_form');
    var commentDeleteForm = document.getElementById('comment_delete_form');
    if (commentEditForm && commentDeleteForm) {
        commentEditForm.addEventListener('submit', function() {
            showCommentAlert('edited'); // Call showCommentAlert function when the form is submitted
        });
        commentDeleteForm.addEventListener('submit', function() {
            showCommentAlert('deleted'); // Call showCommentAlert function when the form is submitted
        });
    }

    // Toggle navigation links visibility when the hamburger button is clicked
    const navbarToggler = document.querySelector('.navbar-toggler');
    const nav = document.querySelector('nav');
    if (navbarToggler && nav) {
        navbarToggler.addEventListener('click', function() {
            nav.classList.toggle('active');
        });
    }

    // Show footer when user scrolls to the bottom
    window.addEventListener("scroll", function() {
        var footer = document.getElementById("site-footer");
        var scrollPosition = window.innerHeight + window.pageYOffset;
        var documentHeight = document.body.offsetHeight;

        // Show footer when user scrolls to the bottom
        footer.style.display = (scrollPosition >= documentHeight) ? "block" : "none";
    });
});

// Function to display alert message
function showAlert() {
    alert('Your RSVP has been confirmed!');
}

// Function to display alert message for comment actions
function showCommentAlert(action) {
    alert('Your comment has been ' + action + ' successfully!');
}
