const form_error_button = document.getElementById("alert_form_errors_btn-close");
const form_error_container = document.getElementById("form_errors_container");

form_error_button.addEventListener("click", function() {
    if (form_error_container.style.display === "block") {
        form_error_container.style.display = "none";
    }
});
