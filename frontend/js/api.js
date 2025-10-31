const API_URL = "http://127.0.0.1:8000/api";

async function apiRequest(endpoint, options = {}) {
  const token = localStorage.getItem("access-token");
  const headers = {
    "Content-Type": "application/json",
    ...options.headers,
  };

  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  const response = await fetch(`${API_URL}/${endpoint}`, {
    ...options,
    headers,
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.detail || `HTTP ${response.status}`);
  }

  return response.json();
}

// функции с использованием внутри apiRequest

// 1 login
async function login(credentials) {
  return apiRequest(`token/`, {
    method: "POST",
    body: JSON.stringify(credentials),
  });
}

// 2 получить текущего пользователя
async function getCurrentUsers() {
  return apiRequest("users/");
}

// 3 получение задач
async function getTasks() {
  return apiRequest("tasks/");
}

// делаем функции глобальными
window.login = login;
window.getCurrentUsers = getCurrentUsers;
window.getTasks = getTasks;
