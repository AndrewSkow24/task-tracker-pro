import axios from "axios";

// Базовый url API
const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
  timeout: 10_000,
});

export default api;
