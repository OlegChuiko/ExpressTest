const popupLink2 = document.getElementById("popup-link2");
const popupTwo = document.getElementById("popupTwo");

popupLink2.addEventListener("click", function (event) {
    event.preventDefault(); 
    popupTwo.style.display = "block"; 

});