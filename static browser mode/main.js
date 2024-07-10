const startRecogBtn = document.getElementById("start_recognize");

// Check if the browser supports the Web Speech API
const SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;

if (SpeechRecognition) {
  // Create a new instance of SpeechRecognition
  const recognition = new SpeechRecognition();

  // Set recognition properties
  recognition.continuous = true; // Continuous listening
  recognition.interimResults = false; // Final results only

  // Handle the error event
  recognition.onerror = (event) =>
    console.error("Speech recognition error", event);

  // Handle the result event
  recognition.onresult = (event) => {
    const transcript =
      event.results[event.results.length - 1][0].transcript.trim();
    document.getElementById("result").textContent = `You said: ${transcript}`;

    if (transcript.toLowerCase() === "thank you") {
      recognition.stop();
      recognition.stopped = true;

      document.getElementById("result").textContent += " (Recognition stopped)";
    }
  };

  // Restart recognition when it ends
  recognition.onend = () => {
    console.log("Recognition End");

    // Check if recognition was stopped manually or ended automatically
    if (!recognition.stopped) recognition.start();

    startRecogBtn.style.display = "block";
  };

  startRecogBtn.addEventListener("click", () => {
    recognition.stopped = false;
    recognition.start();

    startRecogBtn.style.display = "none";
    document.getElementById("result").textContent = "";
  });

  // Start the recognition
  recognition.stopped = false;
  recognition.start();

  startRecogBtn.style.display = "none";
} else {
  console.error("Web Speech API is not supported in this browser.");
}
