
  AOS.init();
// Dark Mode Toggle with OS preference + localStorage
const toggleBtn = document.getElementById('darkModeToggle');
const body = document.body;

function setDarkMode(isDark) {
  body.classList.toggle('dark', isDark);
  localStorage.setItem('darkMode', isDark ? 'enabled' : 'disabled');
  toggleBtn.textContent = isDark ? '☀️ Light Mode' : '🌙 Dark Mode';
  toggleBtn.setAttribute('aria-pressed', String(isDark));
}

function initTheme() {
  const savedMode = localStorage.getItem('darkMode');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const shouldUseDark = savedMode ? savedMode === 'enabled' : prefersDark;
  setDarkMode(shouldUseDark);
}

toggleBtn.addEventListener('click', () => {
  setDarkMode(!body.classList.contains('dark'));
});

// Initialize theme on page load
initTheme();


  // Animated Hospital Stats
  const counters = document.querySelectorAll('.stat-number');
  counters.forEach(counter => {
    const updateCount = () => {
      const target = +counter.getAttribute('data-target');
      const count = +counter.innerText;
      const increment = Math.ceil(target / 200); // speed of count up

      if (count < target) {
        counter.innerText = count + increment > target ? target : count + increment;
        setTimeout(updateCount, 15);
      } else {
        counter.innerText = target;
      }
    };
    updateCount();
  });
  // Scroll to Top Button functionality
const scrollToTopBtn = document.getElementById("scrollToTopBtn");

window.addEventListener("scroll", () => {
  if (window.scrollY > 300) {
    scrollToTopBtn.style.display = "block";
  } else {
    scrollToTopBtn.style.display = "none";
  }
});

scrollToTopBtn.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});
// Smooth Scroll for "Learn More" Button
document.querySelector('.cta-btn').addEventListener('click', function(e) {
  e.preventDefault(); // Prevent default jump
  const target = document.querySelector(this.getAttribute('href'));
  const headerOffset = 80; // Adjust if you have a fixed header
  const elementPosition = target.getBoundingClientRect().top;
  const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

  window.scrollTo({
    top: offsetPosition,
    behavior: 'smooth'
  });
});

