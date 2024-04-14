// document.addEventListener('DOMContentLoaded', function() {
//     const menuToggle = document.querySelector('.menu-toggle');
//     const menu = document.querySelector('.menu');

//     menuToggle.addEventListener('click', function() {
//       menu.classList.toggle('show');
//     });
//   });
document.addEventListener("DOMContentLoaded", function () {
  const menuButton = document.querySelector(".menu-button");
  const menu = document.querySelector(".menu");
  const menuBtnIcon = document.querySelector(".container-circle");
  const menuBtnIconSvg = document.querySelector(".menu-btn__icon");
  menuButton.addEventListener("click", function () {
    menu.classList.toggle("active");
    if (menu.classList.contains("active")) {
      menuBtnIcon.style.right = "auto";
      menuBtnIcon.style.left = "320px";
    } else {
      menuBtnIcon.style.left = "0";
    }
  });

});


