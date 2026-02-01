document.querySelectorAll("[data-copy]").forEach(btn => {
      btn.addEventListener("click", async () => {
        const text = btn.getAttribute("data-copy");
        try {
          await navigator.clipboard.writeText(text);
          const old = btn.textContent;
          btn.textContent = "Copied!";
          setTimeout(() => btn.textContent = old, 900);
        } catch (e) {
          alert("Copy failed. URL: " + text);
        }
      });
    });

    
(function () {
  const modal = document.getElementById("qrModal");
  const img = document.getElementById("qrImg");
  const title = document.getElementById("qrTitle");
  const openLink = document.getElementById("qrOpen");
  const downloadLink = document.getElementById("qrDownload");

  function openModal(qrUrl, codeText) {
    title.textContent = `QR for ${codeText}`;
    img.src = qrUrl;
    openLink.href = qrUrl;
    downloadLink.href = qrUrl;
    downloadLink.setAttribute("download", `${codeText.replace("/", "")}-qr.png`);

    modal.classList.add("show");
    modal.setAttribute("aria-hidden", "false");
  }

  function closeModal() {
    modal.classList.remove("show");
    modal.setAttribute("aria-hidden", "true");
    img.removeAttribute("src");
  }

  document.querySelectorAll("[data-qr-url]").forEach(btn => {
    btn.addEventListener("click", () => {
      openModal(btn.getAttribute("data-qr-url"), btn.getAttribute("data-qr-title"));
    });
  });

  modal.addEventListener("click", (e) => {
    if (e.target && e.target.getAttribute("data-close") === "qr") closeModal();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeModal();
  });
})();
