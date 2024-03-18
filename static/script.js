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
