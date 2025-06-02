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
  }
});

