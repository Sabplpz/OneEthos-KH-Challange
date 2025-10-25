const carousel = document.getElementById('carousel');
  const slides = carousel.children;
  let index = 0;

  document.getElementById('nextBtn').addEventListener('click', () => {
    index = (index + 1) % slides.length;
    carousel.style.transform = `translateX(-${index * 100}%)`;
  });

  document.getElementById('prevBtn').addEventListener('click', () => {
    index = (index - 1 + slides.length) % slides.length;
    carousel.style.transform = `translateX(-${index * 100}%)`;
  });

  // Optional: Auto-slide every 5 seconds
  setInterval(() => {
    index = (index + 1) % slides.length;
    carousel.style.transform = `translateX(-${index * 100}%)`;
  }, 10000);