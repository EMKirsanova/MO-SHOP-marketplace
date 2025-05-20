const filter_button = document.getElementById("dropdown-filter_button");
const filter_menu = document.getElementById("dropdown-filter_form");

filter_button.addEventListener("click", function() {
    if (filter_menu.style.display === "none") {
        filter_menu.style.display = "block";
    } else {
        filter_menu.style.display = "none";
    }
});
