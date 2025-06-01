const video = document.getElementById("bg-video");
let reversed = false;

video.addEventListener("ended", () => {
  video.classList.add("fade-out");

  setTimeout(() => {
    reversed = !reversed;

    const newSrc = reversed 
      ? "../src/assets/mp4/video-reverso.mp4"
      : "../src/assets/mp4/backgroud_image_cadastro.mp4";

    video.setAttribute("src", newSrc);
    video.load();
    video.play();

    // Remove o fade-out após um pequeno tempo para aplicar fade-in
    setTimeout(() => {
      video.classList.remove("fade-out");
    }, 100);
  }, 1000); // tempo do fade-out (1s)
});
