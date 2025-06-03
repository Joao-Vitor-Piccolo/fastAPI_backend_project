window.addEventListener('scroll', function() {
  const navbar = document.getElementById('navbar');
  const logo = document.getElementById('logo');
  const scrollLimit = window.innerHeight * 0.8;

  if (window.scrollY >= scrollLimit) {
    navbar.classList.add('scrolled');
    logo.classList.add('scrolled');
    logo.src='../src/assets/imgs/sp_icon_preta.png'
  } else {
    navbar.classList.remove('scrolled');
    logo.classList.remove('scrolled');
    logo.src = "../src/assets/imgs/"
  }})

const botao = document.getElementById("menu-btn");
const div = document.getElementById("aside");
const overlay = document.getElementById("overlay");

botao.addEventListener("click", function (event) {
  aside.classList.add("aberto");
  overlay.classList.add("visivel");
  event.stopPropagation();
});

overlay.addEventListener("click", function () {
  aside.classList.remove("aberto");
  overlay.classList.remove("visivel");
});

aside.addEventListener("click", function (event) {
  event.stopPropagation();
});