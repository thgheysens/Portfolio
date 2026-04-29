function toggleTheme(id) {
  const card = document.getElementById(id);
  card.classList.toggle('open');
}

document.querySelector('.burger').addEventListener('click', function() {
  document.querySelector('.menu').classList.toggle('open');
});

document.querySelectorAll('.menu a').forEach(function(link) {
  link.addEventListener('click', function() {
    document.querySelector('.menu').classList.remove('open');
  });
});

window.addEventListener('scroll', function() {
  var sections = document.querySelectorAll('section');
  var navLinks = document.querySelectorAll('.menu a');
  var current = '';

  sections.forEach(function(section) {
    var top = section.offsetTop - 100;
    if (window.scrollY >= top) {
      current = section.getAttribute('id');
    }
  });

  navLinks.forEach(function(link) {
    link.style.color = '';
    link.style.background = '';
    if (link.getAttribute('href') === '#' + current) {
      link.style.color = 'var(--primary)';
      link.style.background = 'rgba(37,99,235,0.06)';
    }
  });
});
