document.addEventListener("DOMContentLoaded", async () => {
  if (!isAuthenticated()) {
    window.location.href = "login.html";
    return;
  }

  try {
    const tasks = await getTasks();
    const list = document.getElementById("tasks-list");
    list.innerHTML = tasks
      .map(
        (task) => `
        <li style="margin: 10px 0; padding: 10px border: 1px solid #ddd">
            <strong>${task.title}</strong>
            <p>${task.description}</p>
            <p>${task.created_at}</p>

        </li>`
      )
      .join();
  } catch (error) {
    alert("Ошибка загрузки задач:" + error.message);
  }
});
