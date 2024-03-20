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
