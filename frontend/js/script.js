URL_API_TOKEN = "http://127.0.0.1:8000/api/token/";

async function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const response = await fetch(URL_API_TOKEN, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      "username": username,
      "password": password,
    }),
  });

  if (response.ok) {
    const tokens = await response.json();
    localStorage.setItem("access_token", tokens.access);
    alert("Успешный вход");
  } else {
    alert("Ошибка авторизации");
  }
}
