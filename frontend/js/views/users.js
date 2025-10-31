document.addEventListener("DOMContentLoaded", async () => {
  if (!isAuthenticated()) {
    window.location.href = "login.html";
    return;
  }

  try {
    const user = await getCurrentUsers();
    const info = document.getElementById("user-info");
    console.log(user);
    info.innerHTML = `
        <p>
            <strong>Имя:</strong> ${user[0].username}
        </p>
        <p>
            <strong>Email:</strong> ${user[0].email}
        </p>
        <p>${user[0].date_joined}</p>
    `;
  } catch (error) {
    alert("Ошибка загрузки профиля:" + error.message);
  }
});
