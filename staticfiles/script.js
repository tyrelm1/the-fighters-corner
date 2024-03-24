document.addEventListener("DOMContentLoaded", function() {
    // Signup form submission
    var signupForm = document.getElementById("signup-form");
    if (signupForm) {
        signupForm.addEventListener("submit", handleSignupFormSubmit);
    }

    // Add event listener to the RSVP form
    var rsvpForm = document.getElementById("rsvpForm");
    if (rsvpForm) {
        rsvpForm.addEventListener("submit", handleRsvpFormSubmit);
    }

    // Add event listeners for comment edit and delete forms
    addCommentFormEventListener("comment_edit_form", "edited");
    addCommentFormEventListener("comment_delete_form", "deleted");

    // Toggle navigation links visibility
    var navbarToggler = document.querySelector(".navbar-toggler");
    var nav = document.querySelector("nav");
    if (navbarToggler && nav) {
        navbarToggler.addEventListener("click", toggleNavLinksVisibility);
    }

    // Show footer when user scrolls to the bottom
    window.addEventListener("scroll", showFooterOnScroll);
});

function handleSignupFormSubmit(event) {
    var password1 = document.getElementById("id_password1").value;
    var password2 = document.getElementById("id_password2").value;

    if (password1.length < 8 || password2.length < 8) {
        event.preventDefault(); // Prevent form submission
        document.getElementById("password-requirements").style.display = "block"; // Show password requirements message
    }
}

function handleRsvpFormSubmit() {
    showAlert("Your RSVP has been confirmed!");
}

function addCommentFormEventListener(formId, action) {
    var commentForm = document.getElementById(formId);
    if (commentForm) {
        commentForm.addEventListener("submit", function() {
            showCommentAlert(action);
        });
    }
}

function showAlert(message) {
    alert(message);
}

function showCommentAlert(action) {
    alert("Your comment has been " + action + " successfully!");
}

function toggleNavLinksVisibility() {
    var nav = document.querySelector("nav");
    if (nav) {
        nav.classList.toggle("active");
    }
}

function showFooterOnScroll() {
    var footer = document.getElementById("site-footer");
    var scrollPosition = window.innerHeight + window.pageYOffset;
    var documentHeight = document.body.offsetHeight;

    // Show footer when user scrolls to the bottom
    if (scrollPosition >= documentHeight) {
        footer.style.display = "block";
    } else {
        footer.style.display = "none";
    }
}
