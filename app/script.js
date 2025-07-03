// Example to send a move to backend
async function sendMove(column) {
  const res = await fetch("/move", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ column })
  });
  const data = await res.json();
  console.log(data);
}
