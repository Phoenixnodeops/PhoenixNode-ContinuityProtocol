document.addEventListener("DOMContentLoaded", function () {
  const dashboard = document.getElementById("dashboard");

  const nodes = ["LXA", "ΦPHX", "7H1R", "MXT", "ΩPHX", "NEX-R", "NRX-7Z"];
  let tick = 0;

  function simulateSignal(node) {
    const drift = (Math.random() * 0.1).toFixed(4);
    const anomaly = (Math.random() * 0.9).toFixed(3);
    const status = anomaly > 0.7 ? "⚠️ Drift Detected" : "✅ Stable";
    return `
      <div class="node-box">
        <h3>${node}</h3>
        <p>Continuity Drift: ${drift}</p>
        <p>Anomaly Signal: ${anomaly}</p>
        <p>Status: ${status}</p>
      </div>`;
  }

  function updateDashboard() {
    dashboard.innerHTML = nodes.map(simulateSignal).join("");
    tick++;
  }

  setInterval(updateDashboard, 4000);
  updateDashboard();
});
