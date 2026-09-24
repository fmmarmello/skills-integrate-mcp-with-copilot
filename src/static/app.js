document.addEventListener("DOMContentLoaded", () => {
  const activitiesList = document.getElementById("activities-list");
  const activitySelect = document.getElementById("activity");
  const signupForm = document.getElementById("signup-form");
  const messageDiv = document.getElementById("message");
  const loginButton = document.getElementById("login-button");
  const loginButtonText = document.getElementById("login-button-text");
  const loginModal = document.getElementById("login-modal");
  const loginForm = document.getElementById("login-form");
  const closeLoginModal = document.getElementById("close-login-modal");
  const teacherStatus = document.getElementById("teacher-status");
  const signupButton = document.getElementById("signup-button");

  const teacherSession = {
    username: null,
    password: null,
  };

  function setMessage(text, type = "info") {
    messageDiv.textContent = text;
    messageDiv.className = type;
    messageDiv.classList.remove("hidden");

    setTimeout(() => {
      messageDiv.classList.add("hidden");
    }, 5000);
  }

  function updateTeacherUI() {
    const isLoggedIn = Boolean(teacherSession.username && teacherSession.password);
    loginButtonText.textContent = isLoggedIn
      ? `Professor: ${teacherSession.username}`
      : "Login do professor";
    teacherStatus.textContent = isLoggedIn
      ? `Logado como ${teacherSession.username}. Você pode gerenciar inscrições.`
      : "Faça login como professor para inscrever ou remover estudantes.";
    teacherStatus.classList.toggle("authenticated", isLoggedIn);

    const inputs = signupForm.querySelectorAll("input, select, button[type='submit']");
    inputs.forEach((element) => {
      if (element.id === "signup-button") {
        element.disabled = !isLoggedIn;
        element.textContent = isLoggedIn ? "Inscrever-se" : "Login obrigatório";
        return;
      }
      element.disabled = !isLoggedIn;
    });
  }

  function openLoginModal() {
    loginModal.classList.remove("hidden");
    loginModal.setAttribute("aria-hidden", "false");
  }

  function closeLoginModalView() {
    loginModal.classList.add("hidden");
    loginModal.setAttribute("aria-hidden", "true");
  }

  async function fetchActivities() {
    try {
      const response = await fetch("/activities");
      const activities = await response.json();

      activitiesList.innerHTML = "";
      activitySelect.innerHTML = '<option value="">-- Selecione uma atividade --</option>';

      Object.entries(activities).forEach(([name, details]) => {
        const activityCard = document.createElement("div");
        activityCard.className = "activity-card";

        const spotsLeft = details.max_participants - details.participants.length;
        const canManage = Boolean(teacherSession.username && teacherSession.password);

        const participantsHTML =
          details.participants.length > 0
            ? `<div class="participants-section">
                <h5>Participantes:</h5>
                <ul class="participants-list">
                  ${details.participants
                    .map(
                      (email) =>
                        `<li><span class="participant-email">${email}</span>${
                          canManage
                            ? `<button class="delete-btn" data-activity="${name}" data-email="${email}">❌</button>`
                            : ""
                        }</li>`
                    )
                    .join("")}
                </ul>
              </div>`
            : `<p><em>Nenhum participante ainda</em></p>`;

        activityCard.innerHTML = `
          <h4>${name}</h4>
          <p>${details.description}</p>
          <p><strong>Horário:</strong> ${details.schedule}</p>
          <p><strong>Disponibilidade:</strong> ${spotsLeft} vagas restantes</p>
          <div class="participants-container">
            ${participantsHTML}
          </div>
        `;

        activitiesList.appendChild(activityCard);

        const option = document.createElement("option");
        option.value = name;
        option.textContent = name;
        activitySelect.appendChild(option);
      });

      document.querySelectorAll(".delete-btn").forEach((button) => {
        button.addEventListener("click", handleUnregister);
      });
    } catch (error) {
      activitiesList.innerHTML =
        "<p>Não foi possível carregar as atividades. Tente novamente mais tarde.</p>";
      console.error("Error fetching activities:", error);
    }
  }

  async function handleLogin(event) {
    event.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;

    try {
      const response = await fetch("/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      });

      const result = await response.json();

      if (response.ok) {
        teacherSession.username = username;
        teacherSession.password = password;
        updateTeacherUI();
        closeLoginModalView();
        loginForm.reset();
        setMessage(`Professor ${username} autenticado com sucesso.`, "success");
      } else {
        setMessage(result.detail || "Credenciais inválidas.", "error");
      }
    } catch (error) {
      console.error("Error log in:", error);
      setMessage("Não foi possível fazer login. Tente novamente.", "error");
    }
  }

  async function handleUnregister(event) {
    if (!teacherSession.username || !teacherSession.password) {
      setMessage("Faça login como professor para remover estudantes.", "error");
      return;
    }

    const button = event.target;
    const activity = button.getAttribute("data-activity");
    const email = button.getAttribute("data-email");

    try {
      const response = await fetch(
        `/activities/${encodeURIComponent(activity)}/unregister?email=${encodeURIComponent(email)}&username=${encodeURIComponent(teacherSession.username)}&password=${encodeURIComponent(teacherSession.password)}`,
        {
          method: "DELETE",
        }
      );

      const result = await response.json();

      if (response.ok) {
        setMessage(result.message, "success");
        fetchActivities();
      } else {
        setMessage(result.detail || "Ocorreu um erro", "error");
      }
    } catch (error) {
      setMessage("Não foi possível cancelar a inscrição. Tente novamente.", "error");
      console.error("Error unregistering:", error);
    }
  }

  signupForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    if (!teacherSession.username || !teacherSession.password) {
      openLoginModal();
      setMessage("Faça login como professor antes de inscrever estudantes.", "error");
      return;
    }

    const email = document.getElementById("email").value;
    const activity = document.getElementById("activity").value;

    try {
      const response = await fetch(
        `/activities/${encodeURIComponent(activity)}/signup?email=${encodeURIComponent(email)}&username=${encodeURIComponent(teacherSession.username)}&password=${encodeURIComponent(teacherSession.password)}`,
        {
          method: "POST",
        }
      );

      const result = await response.json();

      if (response.ok) {
        setMessage(result.message, "success");
        signupForm.reset();
        fetchActivities();
      } else {
        setMessage(result.detail || "Ocorreu um erro", "error");
      }
    } catch (error) {
      setMessage("Não foi possível concluir a inscrição. Tente novamente.", "error");
      console.error("Error signing up:", error);
    }
  });

  loginButton.addEventListener("click", openLoginModal);
  closeLoginModal.addEventListener("click", closeLoginModalView);
  loginForm.addEventListener("submit", handleLogin);

  loginModal.addEventListener("click", (event) => {
    if (event.target === loginModal) {
      closeLoginModalView();
    }
  });

  updateTeacherUI();
  fetchActivities();
});
