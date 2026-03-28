const form = document.getElementById('predict-form');
const result = document.getElementById('result');
const resultBadge = document.getElementById('result-badge');
const submitButton = form.querySelector('button[type="submit"]');

const apiBase = window.location.protocol === 'file:' ? 'http://localhost:5000' : '';

function setResult(message, isError = false, badgeText = 'Ready') {
  result.textContent = message;
  result.classList.remove('result-enter');
  void result.offsetWidth;
  result.classList.add('result-enter');

  result.style.color = isError ? '#fecaca' : '#f8fafc';
  result.style.borderColor = isError ? 'rgba(248, 113, 113, 0.35)' : 'rgba(52, 211, 153, 0.25)';
  result.style.backgroundColor = isError ? 'rgba(244, 63, 94, 0.08)' : 'rgba(16, 185, 129, 0.08)';
  resultBadge.textContent = badgeText;
  resultBadge.style.color = isError ? '#fecaca' : '#86efac';
  resultBadge.style.borderColor = isError ? 'rgba(248, 113, 113, 0.22)' : 'rgba(52, 211, 153, 0.22)';
  resultBadge.style.backgroundColor = isError ? 'rgba(244, 63, 94, 0.08)' : 'rgba(16, 185, 129, 0.08)';
}

function readPayload() {
  const formData = new FormData(form);
  const payload = {};

  for (const [key, value] of formData.entries()) {
    const numericValue = Number(value);
    if (!Number.isFinite(numericValue)) {
      throw new Error(`Please enter a valid number for ${key}.`);
    }
    payload[key] = numericValue;
  }

  return payload;
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  let payload;
  try {
    payload = readPayload();
  } catch (error) {
    setResult(error.message, true);
    return;
  }

  setResult('Running the model. Please wait...', false, 'Loading');
  submitButton.disabled = true;
  submitButton.classList.add('opacity-70', 'cursor-not-allowed');

  try {
    const response = await fetch(`${apiBase}/predict`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || 'Prediction request failed.');
    }

    setResult(`Prediction: ${data.prediction}`, false, 'Success');
  } catch (error) {
    setResult(error.message, true, 'Error');
  } finally {
    submitButton.disabled = false;
    submitButton.classList.remove('opacity-70', 'cursor-not-allowed');
  }
});

setResult('Waiting for input...', false, 'Ready');
