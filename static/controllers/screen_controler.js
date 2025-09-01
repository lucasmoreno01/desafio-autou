const navUpload = document.getElementById("nav-upload");
const navText = document.getElementById("nav-text");
const uploadDiv = document.getElementById("upload");
const textDiv = document.getElementById("text");

navUpload.addEventListener("click", () => {
  uploadDiv.style.display = "flex";
  textDiv.style.display = "none";
  navUpload.classList.add("active");
  navText.classList.remove("active");
});

navText.addEventListener("click", () => {
  uploadDiv.style.display = "none";
  textDiv.style.display = "block";
  navUpload.classList.remove("active");
  navText.classList.add("active");
});
