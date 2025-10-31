document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("login-form");
  const errorDiv = document.getElementById("error");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    errorDiv.textContent = "";

    const formData = new FormData(form);
    const credentials = Object.fromEntries(formData);

    try {
      const data = await login(credentials);
      saveToken(data.access);
      window.location.href = "tasks.html";
    } catch (error) {
      errorDiv.textContent = error.message;
    }
  });
});
