async function checkStatus() {
  const res = await fetch("/");
  const data = await res.json();
  document.getElementById("statusBox").textContent = JSON.stringify(data, null, 2);
}

async function sendEcho() {
  const msg = document.getElementById("msgInput").value;
  const res = await fetch("/echo", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message: msg})
  });
  const data = await res.json();
  document.getElementById("echoBox").textContent = JSON.stringify(data, null, 2);
}