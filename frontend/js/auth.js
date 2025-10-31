function isAuthenticated() {
  return !!localStorage.getItem("access_token");
}

function logout() {
  localStorage.removeItem("access_token");
  window.location.href = "login.html";
}

function saveToken(token) {
  localStorage.setItem("access_token", token);
}
