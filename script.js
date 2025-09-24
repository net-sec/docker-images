const image = document.getElementById("image");

async function loadImages() {
  const response = await fetch("/list");
  const images = await response.json();

  function showRandomImage() {
    const randomImage = images[Math.floor(Math.random() * images.length)];
    iamge.src = `/images/${randomImage}`;
  }

  zeigeZufallsbild();
  setInterval(showRandomImage, 10000);
}

loadImages();