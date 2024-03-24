document.addEventListener("DOMContentLoaded", function() {
  
    document.getElementById("signup-form").addEventListener("submit", function(event) {
        var password1 = document.getElementById("id_password1").value;
        var password2 = document.getElementById("id_password2").value;

        if (password1.length < 8 || password2.length < 8) {
            event.preventDefault();
            document.getElementById("password-requirements").style.display = "block"; 
        }
    });

    var rsvpForm = document.getElementById('rsvpForm');
    if (rsvpForm) {
        rsvpForm.addEventListener('submit', function() {
            showAlert();  
        });
    }


    var commentEditForm = document.getElementById('comment_edit_form');
    var commentDeleteForm = document.getElementById('comment_delete_form');
    if (commentEditForm && commentDeleteForm) {
        commentEditForm.addEventListener('submit', function() {
            showCommentAlert('edited'); 
        });
        commentDeleteForm.addEventListener('submit', function() {
            showCommentAlert('deleted'); 
        });
    }

    var navbarToggler = document.querySelector('.navbar-toggler');
    var nav = document.querySelector('nav');
    if (navbarToggler && nav) {
        navbarToggler.addEventListener('click', function() {
            nav.classList.toggle('active');
        });
    }

    window.addEventListener("scroll", function() {
        var footer = document.getElementById("site-footer");
        var scrollPosition = window.innerHeight + window.pageYOffset;
        var documentHeight = document.body.offsetHeight;

        
        footer.style.display = (scrollPosition >= documentHeight) ? "block" : "none";
    });
});


function showAlert() {
    alert('Your RSVP has been confirmed!');
}


function showCommentAlert(action) {
    alert('Your comment has been ' + action + ' successfully!');
}
