(function () {
  const map = {
    "id_username": "e.g. rohan_1122",
    "id_password1": "Create a password",
    "id_password2": "Repeat password"
  };

  Object.entries(map).forEach(([id, placeholder]) => {
    const el = document.getElementById(id);
    if (el) {
      el.setAttribute("placeholder", placeholder);
    }
  });
})();