document.addEventListener("DOMContentLoaded", function () {
  const menuButton = document.querySelector(".menu-button");
  const menu = document.querySelector(".menu");
  const menuBtnIcon = document.querySelector(".container-circle");

  if (!menu.classList.contains("active")) {
    menu.classList.add("active");
    menuBtnIcon.style.right = "auto";
    menuBtnIcon.style.left = "320px";
  }

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