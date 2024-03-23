//signup form submission//
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("signup-form").addEventListener("submit", function(event) {
        var password1 = document.getElementById("id_password1").value;
        var password2 = document.getElementById("id_password2").value;

        if (password1.length < 8 || password2.length < 8) {
            event.preventDefault(); // Prevent form submission
            document.getElementById("password-requirements").style.display = "block"; // Show password requirements message
        }
    });
});

// Function to display alert message
function showAlert() {
    alert('Your RSVP has been confirmed!');
}

// Add event listener to the form submission
document.addEventListener('DOMContentLoaded', function() {
    // Get the RSVP form
    var rsvpForm = document.getElementById('rsvpForm');
    if (rsvpForm) {
        // If the RSVP form exists, add an event listener to it
        rsvpForm.addEventListener('submit', function() {
            showAlert();  // Call the showAlert function when the form is submitted
        });
    }
});

// Function to display alert message for comment actions
function showCommentAlert(action) {
    alert('Your comment has been ' + action + ' successfully!');
}

document.addEventListener("DOMContentLoaded", function() {
    // Add event listener for comment edit form submission
    var commentEditForm = document.getElementById('comment_edit_form');
    if (commentEditForm) {
        commentEditForm.addEventListener('submit', function() {
            showCommentAlert('edited'); // Call showCommentAlert function when the form is submitted
        });
    }

    // Add event listener for comment delete form submission
    var commentDeleteForm = document.getElementById('comment_delete_form');
    if (commentDeleteForm) {
        commentDeleteForm.addEventListener('submit', function() {
            showCommentAlert('deleted'); // Call showCommentAlert function when the form is submitted
        });
    }
});

// JavaScript for toggling navigation links
document.addEventListener('DOMContentLoaded', function() {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const nav = document.querySelector('nav');
  
    // Toggle navigation links visibility when the hamburger button is clicked
    navbarToggler.addEventListener('click', function() {
      nav.classList.toggle('active');
    });
  });
  
 
// JavaScript to show footer when user scrolls to the bottom
window.addEventListener("scroll", function() {
    var footer = document.getElementById("site-footer");
    var scrollPosition = window.innerHeight + window.pageYOffset;
    var documentHeight = document.body.offsetHeight;
  
    // Show footer when user scrolls to the bottom
    if (scrollPosition >= documentHeight) {
      footer.style.display = "block";
    } else {
      footer.style.display = "none";
    }
  });
  