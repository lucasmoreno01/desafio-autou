const uploadOptionButton = document.getElementById("nav-upload")
const textOptionButton = document.getElementById("nav-text")
const uploadSection = document.getElementById("upload")
const textSection = document.getElementById("text")

uploadOptionButton.addEventListener("click", () =>
  changeSendEmailMode(uploadOptionButton)
)
textOptionButton.addEventListener("click", () =>
  changeSendEmailMode(textOptionButton)
)

function changeSendEmailMode(activeitem) {
  if (activeitem === uploadOptionButton) {
    uploadSection.style.display = "flex"
    textSection.style.display = "none"
  } else if (activeitem === textOptionButton) {
    textSection.style.display = "block"
    uploadSection.style.display = "none"
    uploadOptionButton.classList.remove("active")
  }
}
