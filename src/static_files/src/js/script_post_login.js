window.addEventListener('scroll', function() {
  const navbar = document.getElementById('navbar');
  const navcenter = document.getElementById('nav-center');

  const scrollLimit = window.innerHeight * 0.8;

  if (window.scrollY >= scrollLimit) {
    navbar.classList.add('scrolled');
    nav-center.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
    navcenter.classList.remove('scrolled');
  }
});

