document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("email-form");
  const resultBox = document.getElementById("result-box");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(form);

    const response = await fetch("/classify", {
      method: "POST",
      body: formData
    });

    const data = await response.json();

    if (data.error) {
      resultBox.innerHTML = `<p style="color:red">${data.error}</p>`;
    } else {
      resultBox.innerHTML = `
        <h2>Resultado</h2>
        <p><b>Arquivo:</b> ${data.filename}</p>
        <p><b>Categoria:</b> ${data.category}</p>
        <p><b>Resposta sugerida:</b> ${data.response}</p>
      `;
    }
  });
});
