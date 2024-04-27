window.onload = function() {
    window.history.pushState(null, null, window.location.href);
    window.onpopstate = function() {
        window.history.pushState(null, null, window.location.href);
    };
};

document.addEventListener("DOMContentLoaded", function() {
    var submitBtn = document.getElementById("submit-btn");
    var popup = document.getElementById("popup");
    var cancelBtn = document.querySelector(".link_cancel");
    

    submitBtn.addEventListener("click", function() {
        popup.style.display = "block";
    });

    cancelBtn.addEventListener("click", function() {
        popup.style.display = "none";
    });
});