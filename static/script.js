// Auto-refresh status setiap 5 detik
setInterval(() => {
  fetch("/perintah")
    .then(response => response.json())
    .then(data => {
      const statusElem = document.getElementById("status");
      statusElem.textContent = data.perintah;
      statusElem.className = "status " + data.perintah;
    });
}, 5000);